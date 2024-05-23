CREATE TABLE IF NOT EXISTS title_basics (
    tconst VARCHAR(10) NOT NULL PRIMARY KEY,
    title_type titletype,
    primary_title TEXT,
    original_title TEXT,
    is_adult BOOLEAN,
    start_year SMALLINT,
    end_year SMALLINT,
    runtime_minutes INTEGER
);

CREATE TABLE IF NOT EXISTS name_basics (
    nconst VARCHAR(10) NOT NULL PRIMARY KEY,
    primary_name TEXT,
    birth_year SMALLINT,
    death_year SMALLINT
);

CREATE TABLE IF NOT EXISTS professions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(25) UNIQUE
);

CREATE TABLE IF NOT EXISTS genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) UNIQUE
);

CREATE TABLE IF NOT EXISTS film_genres (
    tconst VARCHAR(10) NOT NULL REFERENCES title_basics,
    genre_id SERIAL REFERENCES genres,
    PRIMARY KEY (tconst, genre_id)
);

CREATE TABLE IF NOT EXISTS name_professions (
    nconst VARCHAR(10) NOT NULL REFERENCES name_basics,
    profession_id SERIAL REFERENCES professions,
    PRIMARY KEY (nconst, profession_id)
);

CREATE TABLE IF NOT EXISTS title_episode (
    tconst VARCHAR(10) NOT NULL PRIMARY KEY REFERENCES title_basics,
    parent_tconst VARCHAR(10) REFERENCES title_basics,
    season_number SMALLINT,
    episode_number INTEGER
);

CREATE TABLE IF NOT EXISTS title_ratings (
    tconst VARCHAR(10) REFERENCES title_basics,
    average_rating REAL,
    numvotes INTEGER
);

CREATE TABLE IF NOT EXISTS films_writers (
    tconst VARCHAR(10) NOT NULL REFERENCES title_basics,
    nconst VARCHAR(10) NOT NULL REFERENCES name_basics,
    PRIMARY KEY (tconst, nconst)
);

CREATE TABLE IF NOT EXISTS films_directors (
    tconst VARCHAR(10) NOT NULL REFERENCES title_basics,
    nconst VARCHAR(10) NOT NULL REFERENCES name_basics,
    PRIMARY KEY (tconst, nconst)
);

CREATE TABLE IF NOT EXISTS name_knownfor (
    nconst VARCHAR(10) NOT NULL REFERENCES name_basics,
    tconst VARCHAR(10) NOT NULL REFERENCES title_basics,
    PRIMARY KEY (nconst, tconst)
);

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) UNIQUE
);

CREATE TABLE IF NOT EXISTS title_principals (
    tconst VARCHAR(10) NOT NULL REFERENCES title_basics,
    ordering SMALLINT NOT NULL,
    nconst VARCHAR(10) NOT NULL REFERENCES name_basics,
    category_id SERIAL REFERENCES categories,
    job TEXT,
    characters TEXT[],
    PRIMARY KEY (tconst, ordering)
);

create type titletype as enum ('short', 'movie', 'video', 'tvSeries', 'tvShort', 'tvMiniSeries', 'tvEpisode', 'tvMovie', 'tvSpecial', 'tvPilot', 'videoGame');
