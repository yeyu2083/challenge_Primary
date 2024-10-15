#!/bin/bash
newman run ./collections/Challenge_Primary.postman_collection.json \
  --environment ./environments/QA_Automation.postman_environment.json \
  --reporters cli,allure,json \
  --reporter-allure-export ./allure-results/
