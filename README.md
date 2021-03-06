# House Price Prediction API

## Description
This is a simple API that predicts house prices in Boston based on the `inputs` given in the post request.


## Getting Started

Using this API is very simple.
The API can be found on [Rafihatu's Heroku App](https://rafi-predictions.herokuapp.com/) and has just one useful endpoint: [predict](https://rafi-predictions.herokuapp.com/predict)

The predict endpoint takes only `POST` requests and request made to the endpoint should come with `inputs` as part of the request data.

The `inputs` should be a list containing 13 numbers. e.g 
```
import requests
import json


resp = requests.post("https://rafi-predictions.herokuapp.com/predict", 
                     data=json.dumps({"inputs": [[6.320e-03, 
            1.800e+01, 
            2.310e+00, 
            0.000e+00, 
            5.380e-01, 
            6.575e+00, 
            6.520e+01, 
            4.090e+00, 
            1.000e+00, 
            2.960e+02,
            1530e+01, 
            3.969e+02, 
            5.980e+00
            ],
            [
             8.320e-03, 
             1.850e+01, 
             2.310e+00, 
             0.780e+00, 
             5.380e-01, 
             6.575e+00, 
             6.520e+01, 
             8.090e+00, 
             1.000e+00, 
             12.960e+02,
             1530e+01, 
             3.969e+02, 
             5.980e+00
             ]
            ]}))
print(resp.text)
```
The API can also be tested using [Postman](https://www.postman.com) or [Swagger](https://swagger.io)
![Screenshot 2021-07-24 at 9 14 32 AM](https://user-images.githubusercontent.com/61936161/126859408-6100e1a1-0aac-417a-9586-387f5be69615.png)



## License

The MIT License - Copyright (c) 2021 - Rafihatu Bello
