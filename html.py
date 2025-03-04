<!DOCTYPE html>
<html>
  <head>
<style>
#book1 {
  border: 5px outset #c49ee2;
  background-color: #9ea34b;
  text-align: center;
}
</style>
<body>
      
    <h1>Book Store</h1>
     <h2>Name: Book 1</h2>
      <p>Click the button for the description</p>
    <button onclick="book1function()">Press</button>
    <div id="book1">
      <p>Book 1 is about a book inside a book</p>
    </div>
    
    <script>
      function book1function() {
        var x = document.getElementById("book1");
        if (x.style.display ==="none") {
          x.style.display ="block";
        } else {
          x.style.display ="none";
        }
      }
    </script>
    
</body>

  
</html>
