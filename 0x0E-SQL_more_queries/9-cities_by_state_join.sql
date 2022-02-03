-- lists all cities contained in database
-- each record should display cities id name and states name
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON state_id = states.id;
