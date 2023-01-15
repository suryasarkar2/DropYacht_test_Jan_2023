# Surya Sarkar's assessment

`Trades.data` is a large CSV file that contains a list of trade messages, one per line in the
 following format:

`Time of trade message, CompanyName, Order Type - New order (D) or Cancel (F), Quantity`

The lines are time ordered although two or more lines may have the same time.

Here are some example lines:

`2015-02-28 07:58:14,Bank of Mars,D,140`

`2015-02-28 08:00:14,Bank of Mars,D,200`

`2015-02-28 08:01:13,Bank of Mars,F,200`

`2015-02-28 08:04:29,Joe traders,D,110`

`2015-02-28 08:05:22,Joe traders,F,11`

`2015-02-28 08:05:25,Joe traders,D,70`

Company names will not contain any commas. Ignore any lines which are not properly formatted and continue to process
the rest of the file.

If, in any given 60 second period and for a given company, the ratio of the cumulative quantity of cancels to cumulative
 quantity of orders is greater than 1:3 then the company is engaged in excessive cancelling.

Consider the above lines. During the period 08:00:14 to 08:01:13 `Bank of Mars` made 400 new orders and cancels,
of which 200 were cancels. This is 50% and is excessive cancelling. `Joe traders` did not engage in excessive cancelling.

During the period 08:00:14 to 08:01:13 the Company `Bank of Mars` engaged in excessive cancelling. In this period 50%
of trades `Bank of Mars` submitted, by quantity, were cancels.

## Your Task

You are required to parse the [Trades.data](Trades.data) file and implement **ALL** the functions in the [checker/excessive_cancellations_checker.py](checker/excessive_cancellations_checker.py) file.

The unit tests in the [test/test_excessive_cancellations_checker.py](test/test_excessive_cancellations_checker.py) class should pass if the functions
in [checker/excessive_cancellations_checker.py](checker/excessive_cancellations_checker.py) are implemented correctly.

## Requirements

The [Trades.data](Trades.data) file and the [test/test_excessive_cancellations_checker.py](test/test_excessive_cancellations_checker.py) class should not be modified. If you would like
to add your own unit tests, you can add these in a separate file.

The [requirements.txt](requirements.txt) file should only be modified in order to add any third-party dependencies required for your solution. <br> Please note that all third-party dependencies required for your solution **MUST** be added to the [requirements.txt](requirements.txt) file.

The `pytest` version should not be changed.

Your solution must use/be compatible with `Python version 3.8`. 

##

Good luck!

## License

At CodeScreen, we strongly value the integrity and privacy of our assessments. As a result, this repository is under exclusive copyright, which means you **do not** have permission to share your solution to this test publicly (i.e., inside a public GitHub/GitLab repo, on Reddit, etc.). <br>

## Submitting your solution

Please push your changes to the `main branch` of this repository. You can push one or more commits. <br>

Once you are finished with the task, please click the `Submit Solution` link on <a href="https://app.codescreen.com/candidate/b1fe1c70-f297-45bb-80fb-187b5a0d0ec4" target="_blank">this screen</a>.