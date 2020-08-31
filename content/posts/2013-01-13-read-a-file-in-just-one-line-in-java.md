---
date: "2013-01-13T00:00:00Z"
excerpt: The shortest way to read a file
draft: false
share: true
tags:
- java
title: Read a file in just one line with Java
---


Something I never really liked in Java was the excessive amount of code to just read a file, but finally, starting from Java 1.7 version, there is the following way to do it

{{< highlight java >}}
String content = newScanner(new File(absoluteFilePath)).useDelimiter("\\Z").next();
{{< / highlight >}}

This piece of code misses some important features, like exceptions management, but it finally makes sense for me.

The following is a practical example that uses the [try-with-resources](http://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html) statement to automatically close the opened resource (that comes with Java 1.7 as well) and delegate the exception management to the caller:

{{< highlight java >}}
public String readFileToString(String filePath) throws IOException{
	Path path = Paths.get(filePath);
	String string = "";
	try(Scanner scanner = new Scanner(path))
	{
		string = scanner.useDelimiter("\\A").next();
	}
	return string;
}
{{< / highlight >}}


Following is the same behavior implemented with the older version, much longer to write.

{{< highlight java >}}
public String readFileToString(String filePath){
	String fileContent = "";

	FileReader file = null;

	try{
		file = new FileReader(filePath);
		BufferedReader reader = new BufferedReader(file);
		String line = "";
		while ((line = reader.readLine()) != null) {
			fileContent += line + "\n";
		}
	} catch (IOException e) {
		e.printStackTrace();
	} finally {
		if (file != null) {
			try {
				file.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}

	return fileContent;
}
{{< / highlight >}}
