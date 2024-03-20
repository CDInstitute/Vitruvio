# Copyright (c) 2024 Alberto Tono

import numpy as np
import trimesh
import math 
from scipy.spatial.transform import Rotation as R
import open3d as o3d
import os
import argparse 

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)  
    return allFiles

def ground_vertices(mesh):
    """From a mesh get the main vertices on the ground"""
    mesh_vertices= mesh.vertices                  # get vertices
    mv_z = mesh_vertices[:,1]                     # trimesh import X, Z, -Y
    mv_z_array = np.array(mv_z)                   # translate to array
    mv_z_array = np.round_(mv_z_array, decimals=6, out=None) # IMPORTANT
    min_z_idx = np.argmin(mv_z_array)             # get min indices
    min_z_value = mv_z_array[min_z_idx]           # get min value
    mask = (mv_z_array == min_z_value)            # get mask
    list_z_min_idx = np.where(mask)               # filter values
    mv_ground = mesh_vertices[list_z_min_idx]     # get vertices on the ground
    return mv_ground 

def center_xy(mesh, mesh_path, path_write):
    """Center all meshes"""
    gv = ground_vertices(mesh) #take ground vertices
    centroid = gv.mean(axis=0) # find the centroid
    centroid[1]=0
    main_center = np.array([0,0,0])
    t = centroid - main_center # find translation
    mesh_open3d = o3d.io.read_triangle_mesh(mesh_path) #apply translation to all vertices
    mesh_translated_open3d = mesh_open3d.translate(-t, relative=True) #TODO - brings closer, + move away
    o3d.io.write_triangle_mesh(path_write, mesh_translated_open3d)

def find_principle_axis(points, naxis=2):
    """Compute single principle axis for points"""
    points[:,1]=0                                 # make them with 0 z in the inertia 
    inertia = points.T @ points
    evals, evecs = np.linalg.eig(inertia)
    order = np.argsort(evals)[::-1]               # return largest vectors based on naxis
    return evecs[:, order[:naxis]].T

def axis_on_xy(principal_axis):
    """Get axis only on xy remove the z"""
    indx = np.where(principal_axis[:, 1] == 0 )   # find index of zero
    xy_pr_axis = principal_axis[indx]
    return xy_pr_axis

def assign_sign(principal_axis):
    """Get sign of the rotation wrt y"""
    xy_pr_axis = axis_on_xy(principal_axis)
    xs = xy_pr_axis[:, 0]
    ys = xy_pr_axis[:, 2]
    sign = 0
    if xs[0] > 0 and ys[0]>0: 
        sign = -1
    elif xs[0] < 0 and ys[0]<0:
        sign = 1
    elif xs[0] < 0 and ys[0]>0:
        sign = 1
    elif xs[0] > 0 and ys[0]<0:
        sign = -1
    return sign

def get_rotation_angle(vector_y, principal_axis, degree='degree'):
    """Get rotation angle form vector y in trimesh, and main axis"""
    dot_product = np.dot(vector_y, principal_axis)
    angle_radians = np.arccos(dot_product)
    angle_degree = math.degrees(angle_radians)
    if degree == 'degree': 
        return angle_degree
    elif degree == 'radians': 
        return angle_radians

def rotate_building(angle, mesh_path, path_write):
    """Rotate Building"""
    r = R.from_euler('y', angle, degrees=True)          # x,z,-y so it should be correct
    r = r.as_matrix()
    mesh_open3d = o3d.io.read_triangle_mesh(mesh_path)
    mesh_rotate_open3d = mesh_open3d.rotate(r,center=(0,0,0))
    o3d.io.write_triangle_mesh(path_write, mesh_rotate_open3d)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='This algorithm Center and Align your .objs file, and \
            it also create a .txt keeping track of the orientation, and rotation \
            angle with respect to the North'
    )
    parser.add_argument('--objs', type=str, help='Path to obj files')
    #parser.add_argument('output_objs',type=str, help='Path to output obj files.')
    args = parser.parse_args()
    
    
    folder_path = args.objs  #'/home/alberto/Documents/NDP/notebooks/'
    #path_write = args.output_objs #'/home/alberto/Documents/NDP/notebooks/'

    buildings = getListOfFiles(folder_path)
    
    # CENTER BUILDING
    for i in buildings: 
        #print(i)
        if i[-4:] =='.obj':
            path = os.path.join(folder_path, i) 
            mesh = trimesh.load(path)
            mesh = mesh.bounding_box_oriented
            center_xy(mesh, path, path)
            print("Buildings Centered respect to XY")
            
    vector_y = [0, 0, 1]
    dict_rotations = {}
    for i in buildings: 
        #print(i)
        if i[-4:] =='.obj':
            path = os.path.join(folder_path, i) 
            print('path:', path)
            mesh = trimesh.load(path)
            # 1) get bounding box oriented
            mesh = mesh.bounding_box_oriented 
            print('bbo:', mesh)
            # 2) Find ground vertices
            mv_ground_points = ground_vertices(mesh)
            print('mv_ground_points are:', mv_ground_points)
            # 3) Extract principal axis, same as '-mesh.principal_inertia_vectors[0]' in trimesh
            principal_axis = find_principle_axis(mv_ground_points, naxis=3)
            print('principal axis are:',principal_axis)
            # 4) Get Rotation angle 
            sign = assign_sign(principal_axis)
            print('sign:', sign)
            angle = get_rotation_angle(vector_y, principal_axis[0], 'degree') #principal_axis[0]
            angle = angle * sign 
            # 5) Save Rotation angle
            print('angle is:',angle)
            dict_rotations[i[:-10]] = angle #remove /model.obj
            rotate_building(angle, path, path)
            print('Building as being align to canonical pose')
            
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Specify the file name
    file_name = 'rotation_tracker.txt'
    file_path = os.path.join(folder_path, file_name)
    print('Rotation Tracker File created', file_path)
    
    with open(file_path, 'w') as file:
    # file = open("rotation_tracker.txt","w")
        for key, value in dict_rotations.items(): 
            key = os.path.split(key)[-1]
            file.write('%s:%s\n' % (key, value))
        file.close()
    print("Orientation Saved")