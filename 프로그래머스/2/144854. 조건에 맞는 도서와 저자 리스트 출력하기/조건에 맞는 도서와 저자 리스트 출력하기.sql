-- 코드를 입력하세요
-- select * FROM BOOK;
-- select * FROM AUTHOR;



select book.book_id, author.author_name, DATE_FORMAT(book.published_date,'%Y-%m-%d')as PUBLISHED_DATE
from book  join author where category='경제' and book.author_id = author.author_id order by book.published_date
