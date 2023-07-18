//For every iteration we also perform a nested iteration, hence our code runs double or O(n^2)
function square(n) {
    for (let i=0; i<n; i++) {
        for (let j=0; j<n; j++) {
            console.log(i,j)
        }
    }
}

square(4)