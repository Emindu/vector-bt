Resouces: https://www.youtube.com/watch?v=JOdEZMcvyac&t=698s

## Environment Setups
1. creating virtual environment
    - virtualenv venv
2. Moved to virtual environment 
    - source venv/bin/activate
3. Install vectorBt
    - pip install vectorbt

1. QuickStart
here with one symbol : tutorial1.py
here with multiple symbols: tutorial2.py

with given multiple symbol it can visualized return for multiple symbols with given multiple period

2. Creating Custom Indicators
src: https://vectorbt.dev/api/indicators/factory/ 

how we can create custom indicators
- create custom indicator with just one custom calculation, here calculation was done in function called `custom_indicator` . here only getting values from vectorBT custom Indicator.
    indicator1.py
- create custom indicator with combine builtin indicator values
    indicator2.py
-create time resampled indicator
    indicator3.py 


3. Hyperparameter Optimization

- Mainly we can plot in two ways, 2d(HeatMap) and 3d(Volume)  heatmaps. In Color it shows some metric value such aReturn(such kind of variable)
- Computationally Expensive and Can be over fitted.
- first try, here we are giving parameter values as array and vector bt calculate values with those parameter,
  as example here we are giving parameter as ma_window and rsi_window, here it gives fix array wof parameters.
    optimization1.py
- let's try with range of parameters here
    optimization2.py
- optimization with visualization, here it is visualization with 2d with simple parameters (only 3 can be supported, 2 with parameters with x and y axis, 1 in slider)
    optimization3.py
- optimization with combing values
    optimization4.py
- optimization visualize with volume (cube)
    optimization5.py

4. Optimization Techniques
- Using TA-Lib instead of doing calculation with pandas.
    - Ta-Lib is pre-compiled for machine code (written in c)
    - Installing TA-Lib
        ```
        brew install ta-lib
        pip install TA-Lib

        ```
- loading price data from csv and using TA-Lib, for only 1 assets
    - optiTaLib.py
- for mutiple assets
    - optiTaLib1.py
- with @njit - numba just in compiler for numberical computation optimization
    - optiTaLib2.py
- optimization memory usage- when running large backtests need to optimze memory
    - using batches, this way we can loop variables with different way, in below example it useswindow for looping, this can be optimize with inner looping and further with difeerent symbols 
      - optiTaLib3.py 

5. Graphing/Dashboards 
- portfolio visualizations
	visualize.py
- we can access order details with below ones
	visualize2.py
- custom dashboards
	visualize3.py - using custom fig
	visualize4.py - see the limitations of vbt plot
- here we there are more ways we can use visualizations, which we can utilize, need go throw documentation

6. Order Types

 https://vectorbt.dev/api/portfolio/base/#vectorbt.portfolio.base.Portfolio.from_signals
 we can use above like to give portfolio to use entries with different parameters
- intro to order type- stop loss, take profit, trailing stop loss 
	orderType1.py
- make reverse if market hitting stop loss and taking trade against it
	orderType2.py
- shot only trades 
	orderType3.py
- short and long orders combine
	orderType4.py

7.  Reality Check

here it checks overfitting and undefittings

Techniques
- Split data in to different windows and test for differetn window and getting average
	- window of inputs without average
		vindows.py
	- wndow of inputs with average
		windows2.py
		
- comparing with random buys and sells with our strategy
	- here plotting box plot- for only rsi
	 	compare.py	
	- here it compare with random entries and exits 
		compare2.py

# Prerequisite Learning

## Pandas Align


- note : pandasNote.md
- python: pandasTur.py





