let header = document.querySelector('.header_topbar')
window.onscroll = () => {
    if(pageYOffset >= 1080) {
        header.style.backgroundColor = 'black'
    } else {
        header.style.backgroundColor = 'transparent'
    }
}

let app = () => {
    let categories = document.querySelectorAll('.topbar--item')
    let dishes = document.querySelectorAll('.menu_content__item')

    let filter = (category, items) => {
        items.forEach((item) => {
            let isItemFiltered = !item.classList.contains(category)
            let isShowAll = category.toLowerCase() === 'all'
            if(isItemFiltered && !isShowAll) {
                item.classList.add('hide')
            } else {
                item.classList.remove('hide')
            }
        })
    }
    
    categories.forEach((category) => {
        category.onclick = () => {
            let currentCatrgory = category.dataset.filter
            filter(currentCatrgory, dishes)
        }
    })
}

app()