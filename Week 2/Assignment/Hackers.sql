' Task
Julia conducted a  days of learning SQL contest.
The start date of the contest was March 01, 2016 and the end date was March 15, 2016.
Write a query to print total number of unique hackers who made at least  submission each day (starting on the first day of the contest),
and find the hacker_id and name of the hacker who made maximum number of submissions each day.
If more than one such hacker has a maximum number of submissions, print the lowest hacker_id.
The query should print this information for each day of the contest, sorted by the date.


Read more about the Question here ==> https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem
' ' SOLUTION :
'
SET @date = Null;
SELECT row_n,
    b.d_hackers,
    hacker_id,
    name
FROM (
        SELECT *
        FROM (
                SELECT IF(
                        @date is NULL,
                        @date := sdate,
                        IF(@date = sdate, NULL, @date := sdate)
                    ) as row_n,
                    hacker_id,
                    name
                FROM (
                        Select a.submission_date as sdate,
                            a.r_counter as r_counter,
                            a.hacker_id as hacker_id,
                            c.name as name
                        FROM (
                                Select COUNT(*) as r_counter,
                                    hacker_id,
                                    submission_date
                                FROM Submissions
                                group by hacker_id,
                                    submission_date
                            ) a
                            JOIN (
                                Select *
                                from Hackers
                            ) c ON c.hacker_id = a.hacker_id
                    ) a
                order by sdate,
                    r_counter DESC,
                    hacker_id
            ) a
        WHERE row_n is not null
    ) a
    JOIN (
        SELECT submission_date,
            COUNT(*) as d_hackers
        FROM (
                SELECT DISTINCT(submission_date) as submission_date
                from Submissions
            ) a
            JOIN (
                Select hacker_id
                from Hackers
            ) b ON (
                Select COUNT(DISTINCT(submission_date))
                FROM Submissions
                WHERE submission_date <= a.submission_date
                    and hacker_id = b.hacker_id
                group by hacker_id
            ) = DATEDIFF(a.submission_date, '2016-03-01') + 1
        GROUP BY a.submission_date
    ) b ON b.submission_date = row_n