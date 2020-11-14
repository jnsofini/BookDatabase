CREATE VIEW V_Books
AS
SELECT Book.Title, Book.Publisher, Book.Year, Author.Author_Name 
FROM  Book 
JOIN Author_Book 
ON Author_Book.ISBN=Author_Book.ISBN 
JOIN Author 
ON Author.Author_ID=Author_Book.Author_ID;