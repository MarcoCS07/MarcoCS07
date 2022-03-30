import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def check_row(grid, n, row):
    if all([n != grid[row][i] for i in range(9)]):
        return True
    return False


def check_column(grid, n, column):
    if all([n != grid[i][column] for i in range(9)]):
        return True
    return False


def check_quadrant(grid, n, row, column):
    index_i, index_j = 3 * (row // 3), 3 * (column // 3)
    for i in range(index_i, index_i + 3):
        for j in range(index_j, index_j + 3):
            if grid[i][j] == n:
                return False
    return True


def indexes(grid):
    for i in range(0, grid.shape[0]):
        for j in range(0, grid.shape[1]):
            if grid[i][j] == 0:
                return i, j
    return None, None


def solution(grid, i=None, j=None):
    i, j = indexes(grid)
    if i is None:
        return True

    for number in range(1, 10):
        if check_row(grid, number, i):
            if check_column(grid, number, j):
                if check_quadrant(grid, number, i, j):
                    grid[i][j] = number
                    if solution(grid, i, j):
                        return True
                    grid[i][j] = 0
    return False


def nyt_sudoku():
    """
    Extracts sudoku (easy mode) from New York Times page.
    :return: Numpy array with sudoku's values. 0's are empty cells.
    """

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    sudoku = np.zeros(shape=(9, 9), dtype=int)
    driver = webdriver.Chrome(executable_path=r"E:\Selenium\drivers\chromedriver", options=options)
    driver.get('https://www.nytimes.com/puzzles/sudoku/easy')

    index = 1
    for i in range(9):
        for j in range(9):
            number = driver.find_element_by_xpath(
                xpath='/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div/div/div[' + str(
                    index) + ']'
            )
            if number.get_attribute('aria-label') == 'empty':
                sudoku[i][j] = 0
            else:
                sudoku[i][j] = int(number.get_attribute('aria-label'))
            index += 1

    # Solve sudoku
    print(sudoku)
    solution(sudoku)
    print(sudoku)

    # Write solutions
    index = 1
    for i in range(9):
        for j in range(9):
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div['
                               '1]/div/div/div/div[' + str(index) + ']')))

            if element.get_attribute('aria-label') == 'empty':
                driver.execute_script("arguments[0].click();", element)
                button = WebDriverWait(driver, 20). \
                    until(EC.presence_of_element_located((By.XPATH,
                                                          '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div'
                                                          '[3]/div/div[2]/div[' + str(sudoku[i][j]) + ']')))

                driver.execute_script("arguments[0].click();", button)
                #time.sleep(0.5)
            index += 1

    # 5 secs to enjoy the victory, and we close the navigator
    time.sleep(5)
    driver.close()
    driver.quit()
    return True

# nyt_sudoku()
