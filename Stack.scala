abstract class Stack[A] {
	def push(x: A): Stack[A] = new NonEmptyStack[A](x,this)
	def isEmpty: Boolean
	def top: A
	def pop: Stack[A]
}
class EmptyStack[A] extends Stack[A] {
	def isEmpty = true
	def top = error("EmptyStack.top")
	def pop = error("EmptyStack.pop")
}
class NonEmptyStack[A](elem: A, rest: Stack[A]) extends Stack[A] {
	def isEmpty = false
	def top = elem
	def pop = rest
}
object Stack extends App {	
  var source = scala.io.Source.fromFile(args(0))
  var lines = source.getLines.filter(_.length > 0)
  for (l <- lines) {
	var values = l.split(" ")
	var x = new EmptyStack[String]
	var y = new NonEmptyStack(values(0),x)
	values.foreach {
		value =>  y.push(value)
	}
	var output = ""
	values.foreach {
		value =>
		output += y.pop +" "
	}
	println(output)
  }
}