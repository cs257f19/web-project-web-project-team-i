DROP TABLE IF EXISTS films;
CREATE TABLE films (
  picture text,
  yearOfRelease int,
  nominations int,
  rating float(8),
  duration int,
  genre text,
  subgenre text,
  releaseMonth text,
  criticScore int,
  synopsis text,
);

DROP TABLE IF EXISTS winners;
CREATE TABLE winners (
  yearOfRelease int,
  bestPicture text,
  bestActor text,
  bestActress text,
  bestDirector text,
  actor text,
  actress text,
  director text
);
