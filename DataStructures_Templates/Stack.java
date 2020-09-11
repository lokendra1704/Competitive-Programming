class StackOverFlowException extends Exception {
    StackOverFlowException(String msg) {
        super(msg);
    }
}
class StackUnderFlowException extends Exception {
    StackUnderFlowException(String msg){
        super(msg);
    }
}

public class Stack {
    int[] stack;
    int top;
    int size;
    Stack(){
        this.size = 100;
        this.stack = new int[size];
        this.top = 0;  //Top will be 0 if there are no elements. So if top = 0 and we want to pop, StackUnderFlow Exception is raised
    }
    Stack(int[] arr) throws StackOverFlowException{
        this.size = 100;
        this.stack = new int[size];
        this.top = 0;
        for (int e: arr)
            this.push(e);
    }
    void push(int val) throws StackOverFlowException {
        if (this.top < 100) {
            this.stack[this.top++] = val;
        }
        else {
            throw new StackOverFlowException("Stack is Full. Try Extending the cacpacity by extend() function");
        }
    }
    int pop() throws StackUnderFlowException {
        if (this.top <= 0){
            throw new StackUnderFlowException("Stack is already Empty");
        }
        else {
            int temp = this.stack[--this.top];
            this.stack[top] = 0;
            return temp;
        }
    }

    int peek() throws StackUnderFlowException{
        if (this.top > 0){
            return this.stack[this.top-1];
        }
        else {
            throw new StackUnderFlowException("Stack is Empty");
        }
    }

    void print() throws StackUnderFlowException{
        if (this.top <= 0)
            throw new StackUnderFlowException("Stack is Empty");
        else {
            for(int e: this.stack)
                System.out.print(e+" ");
            System.out.println();
        }
    }

    void extend(){
        this.size = 2*this.size;
        int[] temp = new int[this.size];
        for(int i=0;i<this.stack.length;i++){
            temp[i] = this.stack[i];
        }
        this.stack = temp;
    }

    public static void main(String[] args){
        Stack s1 = new Stack();
        try {
            //Try UnCommenting This Line 
            for(int i=1;i<=100;i++)
                s1.push(i);
            System.out.println(s1.pop());
            s1.push(50);
            System.out.println(s1.peek());
            s1.print();
            s1.extend();
        }
        catch (StackUnderFlowException e) {
            System.out.println(e.getMessage());
        }
        catch (StackOverFlowException e) {
            System.out.println(e.getMessage());
        }
    }

}