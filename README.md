# <img src="Vitruvio_logo.jpg" alt="Vitruvio Icon" width="100" align="left"> Vitruvio: Conditional Variational Autoencoder (CVAE) to Generate Building Meshes via Single Perspective Sketches


![image](https://github.com/CDInstitute/Vitruvio/assets/11828200/35dd6759-3ed8-4d1b-b1da-c833afe09f89)


[Alberto Tono](https://www.linkedin.com/in/albertotono3/)<sup>1,2</sup>,
[Heyaojing Huang](https://www.linkedin.com/in/yaojing-h-0b903620b/)<sup>1</sup>, 
[Ashwin Agrawal](https://www.linkedin.com/in/ashwin-agrawal/)<sup>1</sup>, 
[Martin Fischer](https://www.linkedin.com/in/martin-fischer-5b314/)<sup>1</sup>,

<sup>1</sup>[Stanford University](https://cife.stanford.edu/),
<sup>2</sup>[Computational Design Institute](https://github.com/CDInstitute)

[Paper in Automation in Construction 2024](https://www.sciencedirect.com/science/article/pii/S0926580524002346?dgcid=author)
[Paper in ArXiv 2022](https://arxiv.org/abs/2210.13634)

## Highlights

- We introduced learning-based method for single perspective sketch-to-3D applications in the Architecture Engineering
and Construction (AEC) industry.
- We adapted a previous state-of-the-art Conditional Variational Autoencoder (Occupancy Network) to scalable datasets.
- We showed qualitatively and quantitatively how the building orientation affects the reconstruction.


## Abstract
Today's architectural engineering and construction (AEC) software require a learning curve 
to generate a three-dimension building representation. This limits the ability to quickly 
validate the volumetric implications of an initial design idea communicated via a single sketch.
Allowing designers to translate a single sketch to a 3D building will enable owners to instantly 
visualize 3D project information without the cognitive load required. If previous state-of-the-art 
(SOTA) data-driven methods for single view reconstruction (SVR) showed outstanding results in the 
reconstruction process from a single image or sketch, they lacked specific applications, analysis, 
and experiments in the AEC. Therefore, this research addresses this gap, introducing the first deep 
learning method focused only on buildings that aim to convert a single sketch to a 3D building mesh: Vitruvio. 
Vitruvio adapts Occupancy Network for SVR tasks on a specific building dataset (Manhattan 1K). This adaptation 
brings two main improvements. First, it accelerates the inference process by more than 26% (from 0.5s to 0.37s).
Second, it increases the reconstruction accuracy (measured by the Chamfer Distance) by 18%. During this adaptation
in the AEC domain, we evaluate the effect of the building orientation in the learning procedure since it constitutes 
an important design factor. While aligning all the buildings to a canonical pose improved the overall quantitative metrics,
it did not capture fine-grain details in more complex building shapes (as shown in our qualitative analysis). 
Finally, Vitruvio outputs a 3D-printable building mesh with arbitrary topology and genus from a single perspective sketch, 
providing a step forward to allow owners and designers to communicate 3D information via a 2D, effective, intuitive, 
and universal communication medium: the sketch.

## Presentation

[![Vitruvio Video](https://img.youtube.com/vi/Zgq23GxQKts/0.jpg)](https://youtu.be/Zgq23GxQKts?si=znkTXoYb6kDIjaO3)

## Alignment Algorithm

<img src="GIF_Preparation_white.gif" alt="GIF" width="100" align="left" style="margin-right: 200;"> 

This orientation algorithm aligns buildings to their canonical poses while keeping track of the true north (N) position. Step 2 extracts the Oriented Bounding Box (OBB), and its main axis (𝐼𝑦) is used to perform the orientation in steps 3 and 4. Since we need to keep track of the orientation angle, we create a convention for clockwise and counterclockwise rotations. In step 6, we save the rotation angle for each building in a .txt file named ’Rotation Tracker.txt’.

![Screenshot 2024-06-21 at 10 27 44 AM](https://github.com/CDInstitute/Vitruvio/assets/11828200/810abdc2-8879-456a-9232-131444994042)


## Dataset 

[Dataset, Weights Request & Contribution Form](https://forms.gle/JEUW8kpDz2pmtyYv5) [5GB]

[Dataset Split](https://drive.google.com/file/d/1CA-ck2-E5H8GrK6jvVzKNKVTyM4gCo4Q/view?usp=share_link) [26kb]

## Contact Information
- Alberto Tono : alberto.tono@cd.institute or atono@stanfor.edu

## Cite 

```
@article{TONO2024105498,
        title = {Vitruvio: Conditional variational autoencoder to generate building meshes via single perspective sketches},
        journal = {Automation in Construction},
        volume = {166},
        pages = {105498},
        year = {2024},
        issn = {0926-5805},
        doi = {https://doi.org/10.1016/j.autcon.2024.105498},
        url = {https://www.sciencedirect.com/science/article/pii/S0926580524002346},
        author = {Alberto Tono and Heyaojing Huang and Ashwin Agrawal and Martin Fischer},
        keywords = {Artificial intelligence, Neural-aided design, Deep generative design, Deep generative modeling, Conditional variational autoencoder, Sketch-based modeling},
        abstract = {}
}
```
