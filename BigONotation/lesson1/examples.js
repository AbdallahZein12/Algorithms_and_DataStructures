// This is a linear function because of the foor loop which causes it to be a O(n)
function linearFunc(arr) {
    for (let i=0; i<arr.length; i++) {
        console.log(1000*100000)
    }
}
const arr = [1,2,3,4,5,6,7]
linearFunc(arr)


//This is a constant function because all the statments are evaluated with the same time and do not change with the num of input O(1)
function constants(arr) {
    var result = 100 * 1000
    return result
}