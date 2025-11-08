*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Input Text    username    newuser1
    Input Text    password    pass1234!
    Input Text    password_confirmation    pass1234!
    Click Button    Register
    Page Should Contain    Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Input Text    username    ne
    Input Text    password    pass1234!
    Input Text    password_confirmation    pass1234!
    Click Button    Register
    Page Should Contain    Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Text    username    newuser2
    Input Text    password    pas1!
    Input Text    password_confirmation    pas1!
    Click Button    Register
    Page Should Contain    Password must be at least 8 characters long

# salasana ei sisällä halutunlaisia merkkejä
Register With Valid Username And Invalid Password
    Input Text    username    newuser3
    Input Text    password    password
    Input Text    password_confirmation    password
    Click Button    Register
    Page Should Contain    Password must contain at least one non-letter character



Register With Nonmatching Password And Password Confirmation
    Input Text    username    newuser4
    Input Text    password    pass1234!
    Input Text    password_confirmation    pass12345!
    Click Button    Register
    Page Should Contain    Password and password confirmation do not match

Register With Username That Is Already In Use
    Input Text    username    newuser
    Input Text    password    pass1234!
    Input Text    password_confirmation    pass1234!
    Click Button    Register
    Page Should Contain    Username is already in use



*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  newuser  pass1234!
    Go To Register Page
