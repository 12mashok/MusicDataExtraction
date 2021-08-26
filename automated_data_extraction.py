"""Automates algorithmic input generation from the Numbers into Notes website"""

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

#### Function for Power Series
def powerSeries(base, driver):
	"""This function enters the base number and clicks the button that generates the power series in the website."""
	# Power Series
	power_elem = driver.find_element_by_id("base")
	power_elem.clear()

	power_elem.send_keys(base)

	# Press Power Button
	pow_button = driver.find_element_by_xpath('//*[@title="Generate sequence of powers"]').click()

#### Function for Random Series
def randomSeries(upperLimit, driver):
	"""This function enters the upper limit for the random number generated and clicks the button that generates the random series in the website."""
  
	# Random Series
	random_upperLimit_elem = driver.find_element_by_id("random")
	random_upperLimit_elem.clear()

	random_upperLimit_elem.send_keys(upperLimit)

	# Press Random Button
	random_button = driver.find_element_by_xpath('//*[@title="Generate sequence of random numbers less than the given number"]').click()

#### Function for Fibonacci Series
def fibonacciSeries(fibonacciParam, driver):
	"""This function enters the fibonacci series parameter and clicks the button that generates the random series in the website. Fibonacci series is generated according to the formula """
	# Extract fibonacci parameters. n0 and n1 are the first and second number of the series respectively. k is 

	if len(fibonacciParam) !=3: 
		raise SyntaxError("Incorrect input for fibonacci parameters. fibonacciParam should be of the form [n0, n1, k].")

	n0, n1, k = fibonacciParam

	# Clearning n0 field and entering required number 
	fibonacci_n0_elem = driver.find_element_by_id("n0")
	fibonacci_n0_elem.clear()

	fibonacci_n0_elem.send_keys(n0)

	# Clearning n1 field and entering required number 
	fibonacci_n1_elem = driver.find_element_by_id("n1")
	fibonacci_n1_elem.clear()

	fibonacci_n1_elem.send_keys(n1)

	# Clearning k field and entering required number 
	fibonacci_k_elem = driver.find_element_by_id("k")
	fibonacci_k_elem.clear()

	fibonacci_k_elem.send_keys(k)

	# Press Fibonacci Button
	fibonacci_button = driver.find_element_by_xpath('//*[@title="Generate sequence of Fibonacci numbers"]').click()

#### Function for Prime Series
def primeSeries(driver):
	"""This function clicks the button that generates the prime number series in the website."""
	# Press Primes Button
	primes_button = driver.find_element_by_xpath('//*[@title="Generate sequence of prime numbers"]').click()

#### Function for Pi Series
def piSeries(driver):
	"""This function clicks the button that generates the pi as a series of numbers in the website."""
	# Press Pi Button
	pi_button = driver.find_element_by_xpath('//*[@title="Generate sequence of digits of pi"]').click()

#### Function for Golden Ratio Series
def goldenRatio(driver):
	"""This function clicks the button that generates the Golden Series in the website."""
	# Press Golden Series Button
	golden_series_button = driver.find_element_by_xpath('//*[@title="Generate sequence of digits of the golden ratio"]').click()

def generateAlgoComposition(algorithm, modulo_parameter, series_parameter = ""):
	# initialise input list
	inputs = []

	# open an instance of chrome
	driver = webdriver.Chrome()

	# open specific website
	url = "http://www.numbersintonotes.net/"
	driver.get(url)

	if algorithm == 'fibonacci':
		fibonacciParam = series_parameter
		fibonacciSeries(fibonacciParam, driver)

	elif algorithm == 'primes':
		primeSeries(driver)

	elif algorithm == 'pi':
		piSeries(driver)

	elif algorithm == 'goldenRatio':
		goldenRatio(driver)

	else:
		for index, param in enumerate(series_parameter):
			if algorithm == 'power':
				base = param
				powerSeries(base, driver)

			elif algorithm == 'random':
				upperLimit = param
				randomSeries(upperLimit, driver)

	# Reduce using Modulo 
	modulo_elem = driver.find_element_by_id("modulus")
	modulo_elem.clear()
	modulo_elem.send_keys(modulo_parameter)

	# Press Reduce Button
	reduce_button = driver.find_element_by_xpath('//*[@title="Reduce the numbers to the given modulus"]').click()

	# Press Display Button
	display_button = driver.find_element_by_xpath('//*[@title="Display piano roll"]').click()

	# Get list of notes
	notes = driver.execute_script('''return document.getElementById("notestext").value''')
	# print(index, 'notes: ', type(notes))
	inputs.append(notes)
  
	return inputs


