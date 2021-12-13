# Created by chris at 11/12/2021
Feature: Intervals
  Test vaccine intervals

  Scenario: OK

    Given vaccine pfizer
      And pfizer has 2 doses with 21 day interval
     When I check 2001-01-01 to 2001-01-22 satisfies the pfizer interval
     Then the answer is Yes
