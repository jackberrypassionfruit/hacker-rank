const getNumber = (binary) => {
  let string = '';

  while (binary) {
    string += binary.data;
    binary = binary.next;
  }

  

  return string;
}

console.log(string);