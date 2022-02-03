-- lists all cities of CA that can be found in database
SELECT id, name
FROM cities
WHERE state_id =
      (SELECT id
      FROM states
      WHERE name = 'California')
ORDER BY id ASC;
