# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/alberto/Documents/occupancy_networks/external/mesh-fusion/libfusioncpu

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/alberto/Documents/occupancy_networks/external/mesh-fusion/libfusioncpu/build

# Include any dependencies generated for this target.
include CMakeFiles/fusion_cpu.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/fusion_cpu.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/fusion_cpu.dir/flags.make

CMakeFiles/fusion_cpu.dir/fusion.cpp.o: CMakeFiles/fusion_cpu.dir/flags.make
CMakeFiles/fusion_cpu.dir/fusion.cpp.o: ../fusion.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/alberto/Documents/occupancy_networks/external/mesh-fusion/libfusioncpu/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/fusion_cpu.dir/fusion.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/fusion_cpu.dir/fusion.cpp.o -c /home/alberto/Documents/occupancy_networks/external/mesh-fusion/libfusioncpu/fusion.cpp

CMakeFiles/fusion_cpu.dir/fusion.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/fusion_cpu.dir/fusion.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/alberto/Documents/occupancy_networks/external/mesh-fusion/libfusioncpu/fusion.cpp > CMakeFiles/fusion_cpu.dir/fusion.cpp.i

CMakeFiles/fusion_cpu.dir/fusion.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/fusion_cpu.dir/fusion.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/alberto/Documents/occupancy_networks/external/mesh-fusion/libfusioncpu/fusion.cpp -o CMakeFiles/fusion_cpu.dir/fusion.cpp.s

# Object files for target fusion_cpu
fusion_cpu_OBJECTS = \
"CMakeFiles/fusion_cpu.dir/fusion.cpp.o"

# External object files for target fusion_cpu
fusion_cpu_EXTERNAL_OBJECTS =

libfusion_cpu.so: CMakeFiles/fusion_cpu.dir/fusion.cpp.o
libfusion_cpu.so: CMakeFiles/fusion_cpu.dir/build.make
libfusion_cpu.so: CMakeFiles/fusion_cpu.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/alberto/Documents/occupancy_networks/external/mesh-fusion/libfusioncpu/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libfusion_cpu.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/fusion_cpu.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/fusion_cpu.dir/build: libfusion_cpu.so

.PHONY : CMakeFiles/fusion_cpu.dir/build

CMakeFiles/fusion_cpu.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/fusion_cpu.dir/cmake_clean.cmake
.PHONY : CMakeFiles/fusion_cpu.dir/clean

CMakeFiles/fusion_cpu.dir/depend:
	cd /home/alberto/Documents/occupancy_networks/external/mesh-fusion/libfusioncpu/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/alberto/Documents/occupancy_networks/external/mesh-fusion/libfusioncpu /home/alberto/Documents/occupancy_networks/external/mesh-fusion/libfusioncpu /home/alberto/Documents/occupancy_networks/external/mesh-fusion/libfusioncpu/build /home/alberto/Documents/occupancy_networks/external/mesh-fusion/libfusioncpu/build /home/alberto/Documents/occupancy_networks/external/mesh-fusion/libfusioncpu/build/CMakeFiles/fusion_cpu.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/fusion_cpu.dir/depend

