# Celestia_PFB-UI
Submit PayForBlob Transactions

### Requirements
To build and install, you need to have 

.Python 3.x
.Flask
.pip

### Installation

To install Python 3.x

```console
sudo apt install python3
```

To install Flask
```console
pip install flask

```
To install pip

```console
sudo apt  install python3-pip

```
## Creating a virtual environment and activating

``` mkdir celestiaapp ```

``` cd celestiaapp ```

``` cpython3 -m venv ```

``` source venv/bin/activate ```

## Download the add_block.py app.py index.html

``` wget https://github.com/Yns34/Celestia_PFB-UI/blob/main/add_block.py ```

``` wget https://github.com/Yns34/Celestia_PFB-UI/blob/main/app.py ```

``` mkdir templates ```

``` wget https://github.com/Yns34/Celestia_PFB-UI/blob/main/templates/index.html ```

## Start the Flask

### Run Flask in the celestiaapp folder where the app.py file is located.

``` flask run ```

Open on a web browser and go to http://localhost:5000 to submit payforblob transaction.


