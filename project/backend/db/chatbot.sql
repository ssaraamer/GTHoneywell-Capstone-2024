--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2 (Postgres.app)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: queries; Type: TABLE; Schema: public; Owner: jib
--

CREATE TABLE public.queries (
    datetime integer NOT NULL,
    query text,
    response text
);


ALTER TABLE public.queries OWNER TO jib;

--
-- Name: queries_datetime_seq; Type: SEQUENCE; Schema: public; Owner: jib
--

CREATE SEQUENCE public.queries_datetime_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.queries_datetime_seq OWNER TO jib;

--
-- Name: queries_datetime_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jib
--

ALTER SEQUENCE public.queries_datetime_seq OWNED BY public.queries.datetime;


--
-- Name: queries datetime; Type: DEFAULT; Schema: public; Owner: jib
--

ALTER TABLE ONLY public.queries ALTER COLUMN datetime SET DEFAULT nextval('public.queries_datetime_seq'::regclass);


--
-- Data for Name: queries; Type: TABLE DATA; Schema: public; Owner: jib
--

COPY public.queries (datetime, query, response) FROM stdin;
1	Sample query text	Sample response text
2	Sample query text	Sample response text
\.


--
-- Name: queries_datetime_seq; Type: SEQUENCE SET; Schema: public; Owner: jib
--

SELECT pg_catalog.setval('public.queries_datetime_seq', 2, true);


--
-- Name: queries queries_pkey; Type: CONSTRAINT; Schema: public; Owner: jib
--

ALTER TABLE ONLY public.queries
    ADD CONSTRAINT queries_pkey PRIMARY KEY (datetime);


--
-- PostgreSQL database dump complete
--

