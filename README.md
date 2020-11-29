# Table of Contents  
1. [Description](#description)  
2. [Screenshot](#screenshot)  
3. [Instructions](#instructions)
   1. [How to Run](#how-to-run)
   2. [How to Host](#how-to-host)
4. [Features](#feature-list)

# Description
Collection of finished and "finished" projects to demo in a shiny new webgui using streamlit.

See at: https://portfolio.peti.work

# Screenshot
<img src="https://github.com/pomkos/portfolio/blob/main/sample.png" width="620">

# Instructions
## How to Run

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
## How to Host

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

# Feature list
* [x] Protein calculator [(in prod link)](https://protein.peti.work)
  * [x] Whey cost and content
  * [x] Snack cost and content
  * [x] Option to submit to database
* [x] Venmo requests calculator[(in prod link)](https://payme.peti.work)
  * [x] Customized prefilled venmo link
  * [x] Option to submit to database
* [ ] Covid dashboard (WIP) (see portfolio)
  * [x] Premade plots
  * [x] Usermade plots
    * [x] Group by string variables
    * [x] Date only on x-axis
    * [x] Floats and integers on x-, y-axes but not legend
    * [ ] Scatter, line, bar plots
    * [ ] OLS options for scatterplot
    * [ ] Only categorical variables in legend
    * [ ] Dynamix x/y axis options
    * [ ] Ability to choose countries outside plotly
    * [x] Dynamic plot title
  * [ ] Premade dataset summary
    * [x] Descriptive statistics
    * [ ] Comparative statistics
    * [ ] Predictive statistics
    * [x] Usermade customizable dataset summary
    * [ ] Download customized dataset
  * [ ] Premade heatmaps
  * [ ] Usermade heatmaps
