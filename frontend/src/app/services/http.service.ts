import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable } from 'rxjs';

import { APIResponse } from '../models/api-response';
import { ComparedProductComplete } from '../models/compared.product.complete';
import { Item } from '../models/item.model';
import { Product } from '../models/product.model';

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  url = "http://localhost:5999/api/products"

  constructor(private http: HttpClient) { }

  getAllProducts() {
    return this.http.get<APIResponse<Product>>(`${this.url}`)
      .pipe(catchError(
        (error: Error) => {
          console.log(error);
          return ("404 - Not Found")
        }))
  }


  findProduct(id: number): Observable<Object> {
    return this.http.get<APIResponse<Product>>(`${this.url}/${id}`)
      .pipe(catchError(
        (error: Error) => {
          console.log(error);
          return ("404 - Not Found")
        }))
  }

  compareProduct(id: number): Observable<Object> {
    return this.http.get<APIResponse<ComparedProductComplete>>(`${this.url}/compareProduct/${id}`)
      .pipe(catchError(
        (error: Error) => {
          console.log(error);
          return ("404 - Not Found")
        }))
  }

  findItemsProduct(id: number): Observable<Object> {
    return this.http.get<APIResponse<Item>>(`${this.url}/${id}/items`)
      .pipe(catchError(
        (error: Error) => {
          console.log(error);
          return ("404 - Not Found")
        }))
  }

  productSearch(search: string): Observable<Object> {
    return this.http.get<APIResponse<Item>>(`${this.url}/searchProducts/${search}`)
      .pipe(catchError(
        (error: Error) => {
          console.log(error);
          return ("404 - Not Found")
        }))
  }

}

