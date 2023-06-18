// constructor_concept.kt

fun main(){
	val p = Person(name = "Nipun")
}

class Person(val name: String){
	// {name} is a property here as val/var is used 
	fun getName(){
		println(name)  // name is accessible as its property
	}
}

class Toy(name: String){
	// {name} is a parameter here so not available in sub-closures
	val name2 = name;
	fun getName(){
		println(name)  // name is not accessible here as its property
		println(name2)
	}
}