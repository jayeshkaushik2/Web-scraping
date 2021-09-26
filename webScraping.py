from selenium import webdriver

# browser --> chrome
driver = webdriver.Chrome()

# url for categories of jobs
category = 'https://www.careerguide.com/career-options'
driver.get(category)

# jpb titles will store here
JobTitlesArr = []
# fetching data using classname
jobTitles = driver.find_elements_by_class_name('col-md-4')
for jobTitle in jobTitles:
    try:
        title = jobTitle.find_element_by_class_name('c-font-bold').text
        JobNameList = title.lower().split(' ')
        # initializing job type url
        JobNameUrl = ''
        for i in range(len(JobNameList)):
            if JobNameList[i] == '/':
                JobNameUrl += '+'
            elif JobNameList[i] == '&':
                JobNameUrl += '+'
            else:
                JobNameUrl += JobNameList[i]
        # adding the url to array
        JobTitlesArr.append(JobNameUrl)
    except Exception as e:
        continue

# main job-data the will be fetched from the linkedIn will store in the below array
jobdata = []
for i in range(0, len(JobTitlesArr)):
    jobTitle = JobTitlesArr[i]
    print(jobTitle)
    # linkedIn url for job search
    linkedInUrl = f'https://www.linkedin.com/jobs/search/?keywords={jobTitle}&position=1&pageNum=0'
    # scraping the job page from linkedIn
    driver.get(linkedInUrl)
    # catching the errors
    try:
        # scraping data using class name
        info = driver.find_elements_by_class_name('base-search-card__info')
        # information will store in below array
        details = []
        for post in info:
            # fetching job title name
            jobtitle = post.find_element_by_class_name(
                'base-search-card__title').text

            # fetchin company name
            company = post.find_element_by_class_name(
                'base-search-card__subtitle').text

            # location of company
            location = post.find_element_by_class_name(
                'job-search-card__location').text

            # used for dictionary ease
            jobs = {
                'company': company,
                'job title': jobtitle,
                'job location': location
            }
            details.append(jobs)
        jobdata.append(details)

    except Exception as e:
        continue

# storing the fetched date in a text file
# with open('main.text', 'w') as f:
#     for i in range(len(jobdata)):
#         f.write(str(jobdata[i]))
