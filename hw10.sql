CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child FROM parents AS p, dogs AS d WHERE p.parent = d.name order by -d.height;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs AS d, sizes AS s WHERE height > min AND height <= max;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT p1.child AS sibling1, p2.child AS sibling2, s1.size AS dogsize1, s2.size AS dogsize2
  FROM parents AS p1, parents AS p2, size_of_dogs AS s1, size_of_dogs AS s2
  WHERE p1.parent = p2.parent 
    AND p1.child < p2.child
    AND p1.child = s1.name 
    AND p2.child = s2.name;


-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT 'The two siblings, ' || s.sibling1 || ' and ' || s.sibling2 || ', have the same size: ' ||  dogsize1
  FROM siblings AS s WHERE dogsize1 = dogsize2 AND sibling1 < sibling2; 


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur, (max(height) - min(height)) AS rangeheight
  FROM dogs group by fur HAVING min(height) >= 0.7 * avg(height) AND max(height) <= 1.3 * avg(height);

