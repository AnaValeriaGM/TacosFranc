# Tacos Franc


This project simulates a taco shop. We have our taco-men, orders that are coming in, different types of tacos, a variety of meat to choose from and the ingredients for our tacos.

  - Types: 
    - Tacos, Quesadilla, Mulita, Tostada,Vampiro, Orden
  - Meat:
    - Asada,Adobada, Cabeza, Lengua, Suadero, Veggie,Tripa       
  - Ingredients:
    - Cebolla, Salsa, Cilantro,Aguacate, Frijoles 

# Authors:

- Arturo Lopez: [Turi57](https://github.com/Turi57)
- Raul Aragon: [RaulAT](https://github.com/RaulAT)
- Valeria González: [AnaValeriaGM](https://github.com/AnaValeriaGM)
  
### Support

Tacos Franc used the following to work correctly:

* [PyQT] - Helps with the graphics in a user-friendly way


 Tacos Franc itself is open source with a [public repository][TacosFranc] on GitHub.

### Installation

Tacos Franc requires some extra libraries for it to run:  

[Boto3](https://github.com/boto/boto3) 

It is the amazon web services (AWS) developing software kit (SDK) for python. This module allows python developers to write software that makes use of the amazon services. To install Boto3 we have to write in the terminal:

```sh
  $ pip install boto3
```
Then, we have to set the credentials in an encrypted file:

```sh
      ~/.aws/credentials 
```
 Inside this file we will have:
 
```sh
     [default]
     aws_access_key_id = YOUR_KEY
     aws_secret_access_key = YOUR_SECRET_ACCESS_KEY         
```

After that we have to set the region in the same encrypted folder , but different file: 

```sh
      ~/.aws/config        
```
Inside this file we will have: 
```sh
      [default]
      region=us-east-1      
```
 In python it is important to import boto3 in our file:
 
```sh
      import boto3    
```       
          
In our program we used this library to receive taco orders and to send the corresponding response.

[Json](https://docs.python.org/2/library/json.html)

We used the Json library, Json is a way to structure data for it to be interpreted by any language. To use it the only thing we have to do is import it in our python file: 
```sh
      import json  
```   
 
[Numpy](http://www.numpy.org/)

We used this library because it adds support for large multi-dimension arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. To install this library we need to write the following:
```sh
       pip install "numpy-1.9.2rc1+mkl-cp34-none-win_amd64.whl"
```                    
Then, add it in the python file where it will be used:

```sh
      import numpy
```  
        
[Matplotlib](https://matplotlib.org/)

This library was used to plot, make graphs and tables. To install it we did: 
           
Debian / Ubuntu:
```sh
      sudo apt-get install python-matplotlib
```  
Windows: 
```sh
      python -m pip install -U pip setuptools
      python -m pip install matplotlib
```  
In our python files (where the graphs were made) we imported this library as: 
```sh
      import matplotlib.pyplot
```

#### Others

We also used other libraries that are already installed in python and only have to be imported to the files in which they will be used like: 
- Threading
- Time 
- Queue

### How it works:

![Alt Text](https://github.com/AnaValeriaGM/TacosFranc/blob/master/finalflow2.png)



**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [TacosFranc]: <https://github.com/AnaValeriaGM/TacosFranc/tree/master/CarpetaProyecto>
   [PyQT]: <https://github.com/pyqtgraph/pyqtgraph>




