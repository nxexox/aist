class Stack {
  constructor() {
    this.list = [];
  }

  push(value) {
    this.list.push(value);
  }

  pop() {
    if (!this.isEmpty()) {
      return this.list.pop();
    }
  }

  get() {
    return this.list[this.list.length - 1];
  }

  isEmpty() {
    return this.list.length === 0;
  }
}

const stack = new Stack();

console.log(stack.isEmpty());
stack.push('1');
stack.push('2');
stack.push('3');
console.log(stack.pop());
console.log(stack.get());
console.log(stack.isEmpty());