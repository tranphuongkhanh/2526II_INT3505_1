import "@typespec/http";

using TypeSpec.Http;

@service(#{
  title: "Book Management API"
})
namespace BookAPI;

model Book {
  id?: int32;
  title: string;
  author: string;
  status: "available" | "borrowed";
}

model BookInput {
  title: string;
  author: string;
  status: "available" | "borrowed";
}

model Error {
  success: boolean;
  message: string;
  errors?: string[];
}

// GET /books
@route("/books")
@get
op getBooks(): Book[];

// POST /books
@route("/books")
@post
op createBook(@body input: BookInput): {
  @statusCode status: 201;
};

// GET /books/{id}
@route("/books/{id}")
@get
op getBookById(@path id: int32): Book | Error;

// PUT /books/{id}
@route("/books/{id}")
@put
op updateBook(
  @path id: int32,
  @body input: BookInput
): {
  @statusCode status: 200;
} | Error;

// DELETE /books/{id}
@route("/books/{id}")
@delete
op deleteBook(@path id: int32): {
  @statusCode status: 204;
  success: boolean;
  message: string;
} | Error;