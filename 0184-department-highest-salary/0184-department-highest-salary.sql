# Write your MySQL query statement below
select d.name Department, e.name Employee, salary
from Employee e
join Department d
on e.departmentId = d.id
where e.salary = (select max(salary)
from Employee 
where departmentId = d.id);