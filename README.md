<h1 align="center"> Facial Recognition-based idAM for File Hiding </h1>

<p align="center">
  <a>
    <img src="https://github.com/arjundas1/Facial-recognition-based-idAM-for-File-Hiding/assets/72820515/702fb805-6a89-4d0f-86e4-d8378218ea01" width="550" height="280">
  </a>
</p>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#project-team">Project Team</a></li>
    <li><a href="#methodology">Methodology</a></li>
    <li><a href="#implementation">Implementation</a></li>
    <li><a href="#conclusion">Conclusion</a></li>
  </ol>
</details>

## Introduction
In order to prevent unwanted access to sensitive data and digital assets, modern security
solutions must include Identity and Access Management (idAM). idAM is used to validate a user's
identity and allow access to resources using passwords, access controls, and other
conventional security methods. These precautions have, however, shown to be susceptible to
social engineering and phishing attempts.

The identification issue idAM is facing may have an efficient answer thanks to image
recognition technology. Machine learning algorithms are used in image identification
technologies to interpret visual information, such as facial traits, and accurately identify
people. Organizations may more reliably verify user identities by incorporating picture
recognition technology into idAM, which lowers the risk of illegal access and data breaches.
One of the most popular applications of image recognition technology in idAM is biometric
data, such as facial recognition. In order to verify someone's identification, facial recognition
technology maps their facial traits and compares them to a database of recognized faces. This
technology is a beneficial addition to idAM because it is very dependable and has a low rate of
false positives and false negatives.

Organizations can greatly improve their overall security posture by integrating image
recognition technologies into idAM. The possibility of fraud and data breaches is decreased by
the use of biometric data, which makes sure that only authorized personnel are given access
to critical resources. Image recognition technology is also a scalable solution that can change
to meet the demands of a company as it expands and changes.

A development that has the potential to assist enterprises in preserving the security and integrity of
their digital assets is the incorporation of image recognition technology into idAM. idAM has
the potential to develop into a more dependable and efficient method of identifying users and
allowing access to resources by utilizing the power of machine learning and biometric data.


## Project Team

Guidance Professor: Dr. Chandra Mohan B., School of Computer Science and Engineering, VIT Vellore.

The group for our Information Security Management project consists of -

|Sl.No. | Name  | ID Number |
|-| ------------- |:-------------:|
|1| Mohammad Arqam Shamim | 20BCE2142 |
|2| Arjun Das             | 20BDS0129 |
|3| Manan Sharma          | 20BDS0286 |

## Methodology

LBPH (Local Binary Pattern Histogram) is a Face-Recognition algorithm it is used to
recognize the face of a person. It is known for its performance and how it is able to recognize
the face of a person from both front face and side face. Before starting the intuition behind
the LBPH algorithm, let’s first understand a little bit about the basics of Images and pixels in
order to understand how images are represented before we start the content about FaceRecognition. 

All images are represented in the Matrix formats, which are composed of
rows and columns. The basic component of an image is the pixel. An image is made up of a
set of pixels. Each one of these is a small square. By placing them side by side, we can form
the complete image. A single pixel is considered to be the least possible information in an
image. For every image, the value of pixels ranges between 0 to 255.

When we multiply 32 by 32, the result is 1024, which is the total number of pixels in the
image. Each pixel is composed of Three values R, G, and B, which are the basic colors
red, green, and blue. The combination of these three basic colors will create all these colors
here in the image so we conclude that a single pixel has three channels, one channel for each
one of the basic colors.

Let’s start by analyzing a matrix that represents a piece of the image. As you learned
earlier, an image is represented in these formats. In this example, we have three rows and
three columns and the total number of pixels is nine. Let’s select the central pixel here, value
eight, and apply a condition. If the value is greater or equal to 8, the result is ‘1’ otherwise, if
the value is less than eight, the result is zero. After applying the conditioner, the matrix will
now look like this.
The basic calculation of this algorithm is to apply this condition, selecting the center element
of the matrix. Now we need to generate a binary value. Binary value = 11100010. The
algorithm will start applying the condition from the top left corner element goes up to the 1
element of the 2nd row think like it is making a circle like this.
After converting the Binary value to the decimal value we get Decimal Value = 226. It
indicates that all these pixels around the central value are equal to 226.
This algorithm is robust when it comes to lightning. If you put a flashlight on the image, the
value of the pixels will increase. The higher the values the brighter the image and when values
are lower, the darker the image will be. For this reason, this algorithm has good results in light
and dark images because when the image becomes lighter or darker, all the pixels in the
neighborhood here will be changed. After putting the light on the image the matrix will look
like this. After applying the above condition we will get the binary value the same as above
i.e. 11100010.
Let’s consider this another image here. In order to better understand how the algorithm will
recognize a person’s face
We have the image of a face here, and what the algorithm will do is create several squares, as
you can see here. And within each one of these squares, we have the representation of the
previous light. For example, this square here does not represent only one pixel but is set
with multiple pixels that are three rows and four columns. Three by four is equal to twelve
pixels in total in these squares here in each of these squares that are twelve pixels. And then
we apply that condition to each one. Considering the central pixel
The next step is to create a histogram, which is a concept of statistics that will count how
many times each color appears in each square. This is the representation of the histogram.
For example, if the value 110 appears 50 times a bar like this will be created with this size
equal to 50, if 201 appears 110 times the other bar will be created in this histogram with
this size equal to 100. Based on the comparison of the histograms, the algorithm will be able
to identify the edges and also the corners of the images. For example, in this first square here,
we don’t have information about the person’s face. So, the histogram will be different from
this other square that has the border of the face. In short, the algorithm knows which
histograms represent borders and which histograms represent the person’s main features, such
as the color of the eye, the shape of the mouth, and so on

## Implementation
1. Run the python script face_recognition.py in training mode by passing -train as a command
line argument
It will ask for the name which will be assigned as a label to the recognized face.
It will open the camera and capture 100 pictures of the face to train the face recognition
model using the LBPH face recognition algorithm.
2. Run the Python script face_recognition.py by passing -train as a command line argument
will open the camera and improve the model and test the face recognition abilities.
3. Click the locker.bat file:
a. If the folder is hidden, it will open the camera and try to recognize the face. If the label of
the face recognized matches the password set in a batch file. The hidden folder can be unlocked
and the files inside it can be viewed.
b. If the folder is already unlocked, it will lock and hide the secret folder

## Conclusion

In conclusion, while facial recognition technology holds promise for improving IDAM, it is
important to carefully consider its implementation and potential consequences. There must be
robust safeguards in place to protect the privacy of individuals and prevent misuse of the
technology. Additionally, organizations must be aware of the potential for bias and take steps
to ensure that facial recognition technology is used fairly and equitably. Ultimately, the
success of facial recognition in IDAM will depend on a thoughtful and responsible approach
to its development and deployment.

In the future, the project can be extended to become an application that can run on multiple
operating systems that includes laptops and mobiles. It can be integrated with various security
software as an additional feature.
