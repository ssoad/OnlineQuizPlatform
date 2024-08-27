import random
import time
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

report = Report()
driver = webdriver.Chrome(
    executable_path="C:\\Users\\sohan\\PycharmProjects\\TestingProject\\drivers\\chromedriver.exe")
report.setup(
    report_folder=r'Reports',
    module_name='Login Module',
    release_name='Release 1',
    selenium_driver=driver
)
driver.get('http://sssoad.pythonanywhere.com')

#Test case 1

try:
    # Start of Test
    report.write_step(
        'Navigate to Sign Up Page',
        status=report.status.Start,
        test_number=1
    )
    login = driver.find_element_by_name("signup").click()

    results = driver.current_url
    print(results)
    assert "http://sssoad.pythonanywhere.com/signup/" == results
    report.write_step(
        'Successfully Navigate to Sign Up',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Naviagte Sign Up',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


#Test case 2

try:
    # Start of Test
    report.write_step(
        'Sign Up Test',
        status=report.status.Start,
        test_number=2
    )
    first_name = driver.find_element_by_name("first_name")
    first_name.send_keys("Test")
    last_name = driver.find_element_by_name("last_name")
    last_name.send_keys("User")
    rand = random.randint(0, 100)
    username = driver.find_element_by_name("username")
    username.send_keys(str(rand)+"_test_user")
    email = driver.find_element_by_name("email")
    email.send_keys(str(rand)+"testuser"+str(rand)+"@gmail.com")
    email2 = driver.find_element_by_name("email2")
    email2.send_keys(str(rand)+"testuser"+str(rand)+"@gmail.com")
    password = driver.find_element_by_name("password")
    password.send_keys("test1234")
    organization = driver.find_element_by_name("organization")
    organization.send_keys("UAP")
    role = driver.find_element_by_name("role")
    role.click()
    role.send_keys(Keys.DOWN)
    role.send_keys(Keys.ENTER)
    driver.find_element_by_name("checkbox").click()
    driver.find_element_by_name("signup_btn").click()
    time.sleep(5)
    results = driver.current_url
    print(results)
    assert "Success" in driver.page_source
    report.write_step(
        'Successfully Sign Up (Verification mail sent)',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Sign Up (Verification mail sent)',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )



#Test case 3

try:
    # Start of Test
    report.write_step(
        'Homepage to Login Page',
        status=report.status.Start,
        test_number=3
    )
    login = driver.find_element_by_name("login").click()
    result = driver.current_url
    assert "login" in result
    report.write_step(
        'Successfully on Login page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to reach Login page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


#Test case 4

try:
    # Start of Test
    report.write_step(
        'Examinee Login Test',
        status=report.status.Start,
        test_number=4
    )

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    login = driver.find_element_by_name("login_btn")
    username.send_keys('soad')
    password.send_keys('1234')
    login.send_keys(Keys.ENTER)
    time.sleep(5)
    # drp = driver.find_element_by_id('profiledropdown')
    # drp.send_keys(Keys.ENTER)
    # time.sleep(5)
    # logout = driver.find_element_by_name('logout')
    # logout.send_keys(Keys.ENTER)
    # Test Steps
    results = driver.current_url

    assert "dashboard" in results
    report.write_step(
        'Successfully on Dashboard',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to reach Dashboard',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


#Test Case 5
try:
    # Start of Test
    report.write_step(
        'Logout Test',
        status=report.status.Start,
        test_number=5
    )
    drp = driver.find_element_by_id('profiledropdown')
    drp.send_keys(Keys.ENTER)
    time.sleep(5)
    logout = driver.find_element_by_name('logout')
    logout.send_keys(Keys.ENTER)

    results = driver.current_url
    print(results)
    assert "http://sssoad.pythonanywhere.com/" == results
    report.write_step(
        'Successfully Logged out',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Logout',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


#Test case 6

try:
    # Start of Test
    report.write_step(
        'Login to Create Exam Page',
        status=report.status.Start,
        test_number=6
    )
    driver.find_element_by_name("login").click()
    time.sleep(1)
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    login = driver.find_element_by_name("login_btn")
    username.send_keys('tsr')
    password.send_keys('1234')
    login.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element_by_id("examdropdown").click()
    driver.find_element_by_name("create_exam").click()
    time.sleep(2)
    # time.sleep(5)
    # logout = driver.find_element_by_name('logout')
    # logout.send_keys(Keys.ENTER)
    # Test Steps
    results = driver.current_url

    assert "http://sssoad.pythonanywhere.com/addexam/" == results
    report.write_step(
        'Successfully on Create Exam Page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to navigate Create Exam Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


#Test Case 7
exam_code = random.randint(1, 10000)
day = random.randint(1,30)
try:
    # Start of Test
    report.write_step(
        'Create Exam Test',
        status=report.status.Start,
        test_number=7
    )
    driver.find_element_by_name("exam_title").send_keys("Software Testing : "+str(exam_code))
    driver.find_element_by_name("exam_code").send_keys(exam_code)
    driver.find_element_by_name("exam_marks").send_keys("100");
    dateTime = driver.find_element_by_name("exam_date_time")
    dateTime.send_keys("04042021")
    dateTime.send_keys(Keys.TAB)
    dateTime.send_keys("0245PM")
    driver.find_element_by_name("exam_duration").send_keys("120");
    driver.find_element_by_name("exam_question").send_keys("C:\\pic.jpg");
    time.sleep(5)
    driver.find_element_by_name("exam-btn").click()

    time.sleep(15)
    # time.sleep(5)
    # logout = driver.find_element_by_name('logout')
    # logout.send_keys(Keys.ENTER)
    # Test Steps
    results = driver.current_url

    assert "Exam was successfully created" in driver.page_source
    report.write_step(
        'Successfully on Create Exam Page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to navigate Create Exam Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )
#Test case 8
try:
    # Start of Test
    drp = driver.find_element_by_id('profiledropdown')
    drp.send_keys(Keys.ENTER)
    time.sleep(5)
    logout = driver.find_element_by_name('logout')
    logout.send_keys(Keys.ENTER)
    report.write_step(
        'Join Exam Page',
        status=report.status.Start,
        test_number=8
    )
    driver.get("http://sssoad.pythonanywhere.com/login/")
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    login = driver.find_element_by_name("login_btn")
    username.send_keys('soad')
    password.send_keys('1234')
    login.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element_by_id("examdropdown").click()
    driver.find_element_by_name("join_exam").click()
    print(exam_code)

    ##################
    #driver.find_element_by_name("exam_code").send_keys(int(exam_code))
    ##################

    time.sleep(5)
    #driver.find_element_by_name("joinexam-btn").click()
    # time.sleep(5)
    # logout = driver.find_element_by_name('logout')
    # logout.send_keys(Keys.ENTER)
    # Test Steps
    results = driver.current_url

    assert "JOIN EXAM" in driver.page_source
    report.write_step(
        'Successfully Joined Exam',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Join Exam',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


#Test Case 9


try:
    # Start of Test
    report.write_step(
        'View Exam (Examinee)',
        status=report.status.Start,
        test_number=9
    )
    driver.find_element_by_id("examdropdown").click()
    driver.find_element_by_name("exam_history").click()
    time.sleep(5)


    assert "http://sssoad.pythonanywhere.com/examshistory/" == driver.current_url
    report.write_step(
        'Successfully Navigate to View Exam',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Join Exam',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#Test Case 10
exam_name = ""

try:
    # Start of Test
    report.write_step(
        'Search Exam (Examinee)',
        status=report.status.Start,
        test_number=10
    )
    driver.find_element_by_name("exam_title").send_keys("Django Advanced")
    driver.find_element_by_name("exam_title").send_keys(Keys.ENTER)
    time.sleep(5)

    assert "Django Advanced" in driver.page_source
    report.write_step(
        'Successfully Searched Exam',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Search Exam',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )
#Test Case 11

try:
    # Start of Test
    report.write_step(
        'Download Questions (Examinee)',
        status=report.status.Start,
        test_number = 11
    )
    driver.find_element_by_link_text("Download")
    time.sleep(5)
    url = str(driver.find_element_by_link_text("Download").get_attribute('href'))
    assert len(url)>0
    report.write_step(
        'Successfully Download Question',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Download Question',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


 #Test Case 12

try:
    # Start of Test
    report.write_step(
        'Submit Answer Script (Examinee)',
        status=report.status.Start,
        test_number = 12
    )
    driver.find_element_by_name("answer").send_keys("C:\\test.pdf")
    driver.find_element_by_name("sub-btn").click()
    time.sleep(5)
    url = str(driver.find_element_by_link_text("Download").get_attribute('href'))
    assert len(url)>0
    report.write_step(
        'Successfully Submit Answer Script',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Submit Answer Script',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )   


#Test Case 13

try:
    # Start of Test
    driver.get('http://sssoad.pythonanywhere.com/logout')
    driver.get("http://sssoad.pythonanywhere.com/login")
    report.write_step(
        'Exam History (Examiner)',
        status=report.status.Start,
        test_number = 13
    )
    # driver.find_element_by_name("login").click()
    # time.sleep(1)
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    login = driver.find_element_by_name("login_btn")
    username.send_keys('tsr')
    password.send_keys('1234')
    login.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.get("http://sssoad.pythonanywhere.com/examshistory/")

    
    assert "http://sssoad.pythonanywhere.com/examshistory/" == driver.current_url 
    report.write_step(
        'Successfully Submit Answer Script',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Submit Answer Script',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )
# Test Case 14

try:
    # Start of Test
    report.write_step(
        'Search Specific Exam (Examiner)',
        status=report.status.Start,
        test_number=14
    )
    search = driver.find_element_by_name("exam_title")
    search.send_keys("Django Advanced")
    search.send_keys(Keys.ENTER)
    assert "http://sssoad.pythonanywhere.com/examshistory/" in driver.current_url
    report.write_step(
        'Successfully Search Specific Exam (Examiner)',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Navigate to Search Specific Exam (Examiner)',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 15

try:
    # Start of Test
    report.write_step(
        'View Participant (Examiner)',
        status=report.status.Start,
        test_number=15
    )
    driver.find_element_by_name("view_partcp").click()

    assert "http://sssoad.pythonanywhere.com/participant/" in driver.current_url
    report.write_step(
        'Successfully View Participant (Examiner)',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to View Participant (Examiner)',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 16

try:
    # Start of Test
    report.write_step(
        'View Submission & Download Answer Script (Examiner)',
        status=report.status.Start,
        test_number=16
    )
    driver.back()
    driver.find_element_by_name("view_sub").click()
    time.sleep(5)
    driver.find_element_by_link_text("Download")
    url = str(driver.find_element_by_link_text("Download").get_attribute('href'))
    assert len(url)>0
    report.write_step(
        'Successfully View Submission & Download Answer Script (Examiner)',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to View Submission & Download Answer Script (Examiner)',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 17

try:
    # Start of Test
    report.write_step(
        'Grading (Examiner)',
        status=report.status.Start,
        test_number=17
    )
    driver.find_element_by_name("marks").send_keys(80)
    driver.find_element_by_name("submit_grade").click()
    time.sleep(5)
    assert "Not Graded" not in driver.page_source
    report.write_step(
        'Successfully Graded (Examiner)',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Graded',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 18

try:
    # Start of Test
    report.write_step(
        'View Result, Ranking, Analysis',
        status=report.status.Start,
        test_number=18
    )
    driver.get("http://sssoad.pythonanywhere.com/examshistory/")
    search = driver.find_element_by_name("exam_title")
    search.send_keys("Django")
    search.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element_by_name("view_result").click()
    time.sleep(3)
    driver.back()
    driver.find_element_by_name("view_ranking").click()
    time.sleep(3)
    driver.back()
    driver.find_element_by_name("view_analyse").click()
    time.sleep(3)
    driver.back()
    assert "http://sssoad.pythonanywhere.com/examshistory/" in driver.current_url
    report.write_step(
        'Successfully View Result, Ranking, Analysis',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to View Result, Ranking, Analysis',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 19

try:
    # Start of Test
    report.write_step(
        'Create Profile',
        status=report.status.Start,
        test_number=19
    )
    driver.get("http://sssoad.pythonanywhere.com/createprofile/")
    driver.find_element_by_name("pro_pic").send_keys("C:\\pic.jpg")
    driver.find_element_by_name("contact_number").send_keys("0172273293")
    driver.find_element_by_name("submit-btn").click()
    time.sleep(5)
    driver.get("http://sssoad.pythonanywhere.com/examshistory/")
    assert "You Didn't Create Profile" not in driver.page_source
    report.write_step(
        'Successfully Created Profile',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Create Profile',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


#Test Case 20
try:
    # Start of Test
    report.write_step(
        'Show Profile & Logout',
        status=report.status.Start,
        test_number=20
    )
    driver.get("http://sssoad.pythonanywhere.com/profile/")
    time.sleep(5)
    driver.get("http://sssoad.pythonanywhere.com/logout/")
    assert "http://sssoad.pythonanywhere.com/" == driver.current_url
    report.write_step(
        'Successfully  Show Profile & Logout',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Show Profile & Logout',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )



#Report Generation
report.generate_report()
driver.quit()
