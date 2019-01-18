--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.11
-- Dumped by pg_dump version 9.6.11

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: employee; Type: TABLE; Schema: public; Owner: flaskuser
--

CREATE TABLE public.employee (
    id integer NOT NULL,
    name character varying(250) NOT NULL,
    surname character varying(250) NOT NULL,
    birth_year integer
);


ALTER TABLE public.employee OWNER TO flaskuser;

--
-- Name: employee_id_seq; Type: SEQUENCE; Schema: public; Owner: flaskuser
--

CREATE SEQUENCE public.employee_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.employee_id_seq OWNER TO flaskuser;

--
-- Name: employee_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: flaskuser
--

ALTER SEQUENCE public.employee_id_seq OWNED BY public.employee.id;


--
-- Name: employee id; Type: DEFAULT; Schema: public; Owner: flaskuser
--

ALTER TABLE ONLY public.employee ALTER COLUMN id SET DEFAULT nextval('public.employee_id_seq'::regclass);


--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: flaskuser
--

COPY public.employee (id, name, surname, birth_year) FROM stdin;
1	Zosia	Samosia	\N
2	Jacek	Placek	\N
\.


--
-- Name: employee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: flaskuser
--

SELECT pg_catalog.setval('public.employee_id_seq', 2, true);


--
-- Name: employee employee_pkey; Type: CONSTRAINT; Schema: public; Owner: flaskuser
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

