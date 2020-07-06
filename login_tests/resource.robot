*** Settings ***
Documentation     Robot Keywords

Library           SeleniumLibrary

*** Variables ***
${SERVER}         https://team3-8210-msa.herokuapp.com
${BROWSER}        Firefox
${DELAY}          0
${VALID USER}     instructor
${VALID PASSWORD}    instructor1a
${LOGIN URL}      ${SERVER}/accounts/login/
${WELCOME URL}    ${SERVER}/home/
${ERROR URL}      ${SERVER}/error.html

*** Keywords ***
Open login page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Login Page Should Be Open

Login Page Should Be Open
    Title Should Be    MSA

Go To Login Page
    Go To    ${LOGIN URL}
    Login Page Should Be Open

Input Username
    [Arguments]    ${username}
    Input Text    id_username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    id_password    ${password}

Submit Credentials
    Click Button  xpath:/html/body/div/div/div/div/form/div[3]/div/input

Welcome Page Should Be Open
    Location Should Be    ${WELCOME URL}
    Title Should Be    MSA
