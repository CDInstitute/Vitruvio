Vitruvio: Conditional Variational Autoencoder (CVAE) to Generate Building Meshes via Single Perspective Sketches
![image](https://github.com/CDInstitute/Vitruvio/assets/11828200/35dd6759-3ed8-4d1b-b1da-c833afe09f89)


[Alberto Tono](https://www.linkedin.com/in/albertotono3/)<sup>1,2</sup>,
[Heyaojing Huang](https://www.linkedin.com/in/yaojing-h-0b903620b/)<sup>1</sup>, 
[Ashwin Agrawal](https://www.linkedin.com/in/ashwin-agrawal/)<sup>1</sup>, 
[Martin Fischer](https://www.linkedin.com/in/martin-fischer-5b314/)<sup>1</sup>,

<sup>1</sup>[Stanford University](https://cife.stanford.edu/),
<sup>2</sup>[Computational Design Institute](https://github.com/CDInstitute),

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

## Contact Information
- Alberto Tono : alberto.tono@cd.institute or atono@stanfor.edu

## Cite 

```
@misc{tono22vitruvio,
  doi = {},
  url = {},
  author = {Tono, Alberto; Heyaojing, Huang;  Ashwin, Agrawal; Fischer, Martin},
  title = {Vitruvio: Conditional Variational Autoencoder (CVAE) to Generate Building Meshes via Single Perspective Sketches},
  publisher = {},
  year = {2022},
}
```
