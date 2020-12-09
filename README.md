# Table of Contents  
1. [Description](#description)  
2. [Screenshot](#screenshot)  
3. [How Tos](#how-tos)
   1. [Run](#run)
   2. [Host](#host)


# Description
Collection of finished and "finished" projects to demo in a shiny new webgui using streamlit.

[My Portfolio](https://portfolio.peti.work)

# Screenshot
<img src="https://github.com/pomkos/portfolio/blob/main/sample.png" width="620">

# How Tos
## Run

1. Clone the repository:
```
git clone https://github.com/pomkos/portfolio
cd portfolio
```

2. Create a conda environment (optional):

```
conda create --name "port_env"
```

3. Activate environment, install python, install dependencies.

```
conda activate port_env
conda install python=3.8
pip install -r requirements.txt
```
3. Start the application:
```
streamlit run dash.py
```
5. Access the portfolio at `localhost:8501`
## Host

1. Create a new file outside the `portfolio` directory:

```
cd
nano portfolio.sh
```

2. Paste the following in it, then save and exit:

```
#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh

cd ~/portfolio
conda activate port_env

nohup streamlit run dash.py --server.port 8503&
```

3. Edit crontab so portfolio is started when server reboots

```
crontab -e
```

4. Add the following to the end, then save and exit

```
@reboot /home/portfolio.sh
```

5. Access the portfolio at `localhost:8503`
