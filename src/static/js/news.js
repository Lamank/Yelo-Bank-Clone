let news_item = document.querySelectorAll(".news_item");
let more_news = $('#more_news');
range_num = 3
for(let i = range_num; i<news_item.length; i++){
    news_item[i].style.display = 'none';
}

more_news.click(function () {
    if (range_num < news_item.length) {
        range_num += 3
        for (let i = range_num-3; i < range_num ; i++) {
            news_item[i].style.display='block';
        }
        if (range_num == news_item.length)
        {
            more_news.hide();
        }
    } 
});