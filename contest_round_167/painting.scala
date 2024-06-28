import scala.collection.mutable

object MatrixPainting {

  def main(args: Array[String]): Unit = {
    val sc = new java.util.Scanner(System.in)
    val n = sc.nextInt()
    val m = sc.nextInt()
    val q = sc.nextInt()

    // Store the restrictions
    val restrictedRows = mutable.Map[Int, Char]()
    val restrictedColumns = mutable.Map[Int, Char]()

    // Results to store the minimum costs after each query
    val results = Array.ofDim[Int](q)

    for (i <- 0 until q) {
      val x = sc.nextInt()
      val y = sc.nextInt()
      val c = sc.next().charAt(0)

      var cost = 0

      // Check and update restricted rows
      if (!restrictedRows.contains(x) || restrictedRows(x) == c) {
        restrictedRows(x) = c
      } else {
        cost += 1
      }

      // Check and update restricted columns
      if (!restrictedColumns.contains(y) || restrictedColumns(y) == c) {
        restrictedColumns(y) = c
      } else {
        cost += 1
      }

      // Calculate the cost
      val numRowsRestricted = restrictedRows.size
      val numColsRestricted = restrictedColumns.size
      results(i) = if (numRowsRestricted + numColsRestricted > 1) {
        (numRowsRestricted + numColsRestricted) * (numRowsRestricted + numColsRestricted)
      } else {
        0
      }
    }

    // Output the results
    results.foreach(println)
  }
}
