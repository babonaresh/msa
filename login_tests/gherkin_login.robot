*** Settings ***
Documentation     test suite with BDD and Robot framework style test.

Resource          resource.robot
Test Teardown     Close Browser

*** Test Cases ***
Valid Login
    Given I opened the login page
    When I login with "instructor" and password "instructor1a"
    Then welcome page should be open

*** Keywords ***
I opened the login page
    Open login page

I login with "${username}" and password "${password}"
    Input username    ${username}
    Input password    ${password}
    Submit credentials
