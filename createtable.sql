DROP TABLE IF EXISTS films;
CREATE TABLE films (
  picture text,
  yearOfRelease int,
  rating float(8),
  runtime int,
  genre text,
  subgenre text,
  releaseMonth text,
  score int,
  synopsis text,
);

DROP TABLE IF EXISTS winners;
CREATE TABLE winners (
  yearOfRelease int,
  bestPicture text,
  bestActor text,
  actor text,
  bestActress text,
  actress text,
  bestDirector text,
  director text
);
