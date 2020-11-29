# Portfolio
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
## How to Host Headless

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

# Repo List

All my repos gathered in one place, categorized for easier viewability

__CV Makers__
* [Devfolio](https://github.com/pomkos/devfolio) #fork
* [Markdown-cv](https://github.com/pomkos/markdown-cv) #fork

__Deephire__
* [Prospects](https://github.com/pomkos/prospects) #private
* [Wiscraper](https://github.com/pomkos/wiscraper) #private
* [Angel scraper](https://github.com/pomkos/angel) #private

__Dissertation__
* [Biking](https://github.com/pomkos/biking)
* [Entropy tremor](https://github.com/pomkos/entropy_tremor)
* [Dancing](https://github.com/pomkos/dancing)

__Homserver stuff__
* [Hassio config](https://github.com/pomkos/hassio_config)
* [Homeserver](https://github.com/pomkos/homeserver)

__ML Resources__
* [Learn data science in 3 months](https://github.com/pomkos/Learn_Data_Science_in_3_Months) #fork 
* [Dashboards](https://github.com/pomkos/dashboards) #fork
* [Course resources ML with experts budgets](https://github.com/pomkos/course-resources-ml-with-experts-budgets) #fork

__Personal__
* [Backpacking](https://github.com/pomkos/backpacking)

__Projects__
* [Portfolio](https://github.com/pomkos/portfolio)
* [Brotein](https://github.com/pomkos/brotein)
* [Payme](https://github.com/pomkos/payme)
* [BMSSAC Datacamp](https://github.com/pomkos/BMSSAC_Datacamp) #fork
* [Finished-projects](https://github.com/pomkos/Finished-Projects)
* [Cookpad scraper](https://github.com/pomkos/cookpad_scrape)
* [Flask do](https://github.com/pomkos/flask_do) #archived

__Covid__
* [NYT Covid data](https://github.com/pomkos/nyt-covid-data) #fork
* [John Hopkins Covid data](https://github.com/pomkos/john-hopkins-covid-data) #fork
* [Kaggle Covid19](https://github.com/pomkos/covid19) #archived
* [Covid dash using plotly dash](https://github.com/pomkos/covid_w_plotlydash) #archived

