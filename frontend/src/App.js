import axios from "axios";
import React, {useEffect, useState} from "react";

function App() {
  const [ news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get("http://localhost:8000/api/news/")
    .then(response =>{
      console.log("Fetched news", response.data);
      setNews(response.data);
      setLoading(false);
    })
    .catch(error => {
      console.error("Error fetching news:", error);
      setLoading(false);
    })
  }, []);

  
  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
    <h1>📰 News Dashboard</h1>
    {loading ? <p>Loading news...</p> : (
      <ul>
        {news.length === 0 ? (
          <p>No news available</p>
        ) : (
          news.map((article, index) => (
            <li key={index} style={{ marginBottom: "10px" }}>
              <a href={article.url} target="_blank" rel="noopener noreferrer">
                {article.title} ({article.sentiment})
              </a>
            </li>
          ))
        )}
      </ul>
    )}
  </div>

  );
}

export default App;