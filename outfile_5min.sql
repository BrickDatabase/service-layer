--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

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
-- Name: day; Type: TABLE; Schema: public; Owner: edward_riley
--

CREATE TABLE public.day (
    id integer NOT NULL,
    day integer NOT NULL
);


ALTER TABLE public.day OWNER TO edward_riley;

--
-- Name: day_id_seq; Type: SEQUENCE; Schema: public; Owner: edward_riley
--

CREATE SEQUENCE public.day_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.day_id_seq OWNER TO edward_riley;

--
-- Name: day_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edward_riley
--

ALTER SEQUENCE public.day_id_seq OWNED BY public.day.id;


--
-- Name: information; Type: TABLE; Schema: public; Owner: edward_riley
--

CREATE TABLE public.information (
    id integer NOT NULL,
    subreddit_id integer NOT NULL,
    date timestamp without time zone NOT NULL,
    subscribers integer,
    active_subscribers integer,
    submission integer,
    comments integer
);


ALTER TABLE public.information OWNER TO edward_riley;

--
-- Name: information_id_seq; Type: SEQUENCE; Schema: public; Owner: edward_riley
--

CREATE SEQUENCE public.information_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.information_id_seq OWNER TO edward_riley;

--
-- Name: information_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edward_riley
--

ALTER SEQUENCE public.information_id_seq OWNED BY public.information.id;


--
-- Name: lookup; Type: TABLE; Schema: public; Owner: edward_riley
--

CREATE TABLE public.lookup (
    id integer NOT NULL,
    name character varying(45) NOT NULL,
    abbreviation character varying(45) NOT NULL
);


ALTER TABLE public.lookup OWNER TO edward_riley;

--
-- Name: lookup_id_seq; Type: SEQUENCE; Schema: public; Owner: edward_riley
--

CREATE SEQUENCE public.lookup_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lookup_id_seq OWNER TO edward_riley;

--
-- Name: lookup_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edward_riley
--

ALTER SEQUENCE public.lookup_id_seq OWNED BY public.lookup.id;


--
-- Name: own; Type: TABLE; Schema: public; Owner: edward_riley
--

CREATE TABLE public.own (
    user_id integer NOT NULL,
    subreddit_id integer NOT NULL
);


ALTER TABLE public.own OWNER TO edward_riley;

--
-- Name: users; Type: TABLE; Schema: public; Owner: edward_riley
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(45) NOT NULL,
    password character varying(150) NOT NULL,
    role integer
);


ALTER TABLE public.users OWNER TO edward_riley;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: edward_riley
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO edward_riley;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edward_riley
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: day id; Type: DEFAULT; Schema: public; Owner: edward_riley
--

ALTER TABLE ONLY public.day ALTER COLUMN id SET DEFAULT nextval('public.day_id_seq'::regclass);


--
-- Name: information id; Type: DEFAULT; Schema: public; Owner: edward_riley
--

ALTER TABLE ONLY public.information ALTER COLUMN id SET DEFAULT nextval('public.information_id_seq'::regclass);


--
-- Name: lookup id; Type: DEFAULT; Schema: public; Owner: edward_riley
--

ALTER TABLE ONLY public.lookup ALTER COLUMN id SET DEFAULT nextval('public.lookup_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: edward_riley
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: day; Type: TABLE DATA; Schema: public; Owner: edward_riley
--

COPY public.day (id, day) FROM stdin;
\.


--
-- Data for Name: information; Type: TABLE DATA; Schema: public; Owner: edward_riley
--

COPY public.information (id, subreddit_id, date, subscribers, active_subscribers, submission, comments) FROM stdin;
1	1	2021-04-17 04:07:19	20400	148	35080	325604
2	2	2021-04-17 04:07:22	5074564	17845	2159612	18555196
3	3	2021-04-17 04:07:24	2708605	11203	955742	11203535
4	4	2021-04-17 04:07:26	9825372	153987	1498481	39365081
5	5	2021-04-17 04:07:35	723469	1878	89624	589998
6	6	2021-04-17 04:07:37	73909	223	71136	666915
7	7	2021-04-17 04:07:38	502292	1233	194796	1146786
8	8	2021-04-17 04:07:40	272983	629	108578	626387
9	9	2021-04-17 04:07:49	2076959	1125	213059	3671923
10	10	2021-04-17 04:07:51	29628061	17638	5721059	71532408
11	1	2021-04-17 04:12:22	20400	155	35080	325605
12	2	2021-04-17 04:12:24	5074582	19669	2159616	18555234
13	3	2021-04-17 04:12:26	2708623	11203	955743	11203572
14	4	2021-04-17 04:12:28	9825418	153987	1498482	39365211
15	5	2021-04-17 04:12:35	723472	1878	89624	589999
16	6	2021-04-17 04:12:36	73910	223	71136	666915
17	7	2021-04-17 04:12:38	502292	1364	194796	1146787
18	8	2021-04-17 04:12:41	272983	629	108578	626393
19	9	2021-04-17 04:12:43	2076960	1178	213059	3671925
20	10	2021-04-17 04:12:53	29628076	17460	5721063	71532433
21	1	2021-04-17 04:17:24	20400	155	35080	325605
22	2	2021-04-17 04:17:26	5074589	19669	2159616	18555280
23	3	2021-04-17 04:17:28	2708643	11203	955745	11203599
24	4	2021-04-17 04:17:30	9825464	156613	1498483	39365304
25	5	2021-04-17 04:17:32	723473	1878	89625	590001
26	6	2021-04-17 04:17:39	73910	223	71136	666915
27	7	2021-04-17 04:17:41	502295	1200	194799	1146793
28	8	2021-04-17 04:17:43	272982	629	108578	626395
29	9	2021-04-17 04:17:45	2076961	1176	213059	3671926
30	10	2021-04-17 04:17:47	29628095	17460	5721065	71532477
31	1	2021-04-17 04:22:29	20400	155	35080	325606
32	2	2021-04-17 04:22:53	5074603	19669	2159618	18555323
33	3	2021-04-17 04:22:57	2708667	11203	955745	11203627
34	4	2021-04-17 04:22:59	9825502	155113	1498488	39365427
35	5	2021-04-17 04:23:02	723475	1878	89625	590002
36	6	2021-04-17 04:23:06	73911	259	71136	666915
37	7	2021-04-17 04:23:09	502295	1200	194800	1146798
38	8	2021-04-17 04:23:10	272982	629	108578	626398
39	9	2021-04-17 04:23:14	2076962	1176	213059	3671929
40	10	2021-04-17 04:23:19	29628121	17460	5721067	71532519
\.


--
-- Data for Name: lookup; Type: TABLE DATA; Schema: public; Owner: edward_riley
--

COPY public.lookup (id, name, abbreviation) FROM stdin;
1	Rochester Institute of Technology	rit
2	Minecraft	minecraft
3	Bitcoin	bitcoin
4	Wallstreet Bets	wallstreetbets
5	Robinhood	robinhood
6	GameStop	gamestop
7	Sony PlayStation	playstation
8	Microsoft Xbox	xbox
9	Nintendo	nintendo
10	Gaming	gaming
\.


--
-- Data for Name: own; Type: TABLE DATA; Schema: public; Owner: edward_riley
--

COPY public.own (user_id, subreddit_id) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: edward_riley
--

COPY public.users (id, username, password, role) FROM stdin;
\.


--
-- Name: day_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edward_riley
--

SELECT pg_catalog.setval('public.day_id_seq', 1, false);


--
-- Name: information_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edward_riley
--

SELECT pg_catalog.setval('public.information_id_seq', 40, true);


--
-- Name: lookup_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edward_riley
--

SELECT pg_catalog.setval('public.lookup_id_seq', 10, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edward_riley
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: day day_pk; Type: CONSTRAINT; Schema: public; Owner: edward_riley
--

ALTER TABLE ONLY public.day
    ADD CONSTRAINT day_pk PRIMARY KEY (id);


--
-- Name: information information_pkey; Type: CONSTRAINT; Schema: public; Owner: edward_riley
--

ALTER TABLE ONLY public.information
    ADD CONSTRAINT information_pkey PRIMARY KEY (id);


--
-- Name: lookup lookup_pkey; Type: CONSTRAINT; Schema: public; Owner: edward_riley
--

ALTER TABLE ONLY public.lookup
    ADD CONSTRAINT lookup_pkey PRIMARY KEY (id);


--
-- Name: users user_pk; Type: CONSTRAINT; Schema: public; Owner: edward_riley
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT user_pk PRIMARY KEY (id);


--
-- Name: information fk_lookup; Type: FK CONSTRAINT; Schema: public; Owner: edward_riley
--

ALTER TABLE ONLY public.information
    ADD CONSTRAINT fk_lookup FOREIGN KEY (subreddit_id) REFERENCES public.lookup(id);


--
-- Name: day infold; Type: FK CONSTRAINT; Schema: public; Owner: edward_riley
--

ALTER TABLE ONLY public.day
    ADD CONSTRAINT infold FOREIGN KEY (id) REFERENCES public.information(id);


--
-- Name: own subreddit_id; Type: FK CONSTRAINT; Schema: public; Owner: edward_riley
--

ALTER TABLE ONLY public.own
    ADD CONSTRAINT subreddit_id FOREIGN KEY (subreddit_id) REFERENCES public.lookup(id);


--
-- Name: own user_id; Type: FK CONSTRAINT; Schema: public; Owner: edward_riley
--

ALTER TABLE ONLY public.own
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

