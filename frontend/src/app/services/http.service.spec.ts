import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { TestBed } from '@angular/core/testing';
import { createSpyFromClass, Spy } from 'jasmine-auto-spies';

import { Item } from '../models/item.model';
import { Product } from '../models/product.model';
import { HttpService } from './http.service';


describe('Http Service', () => {
  let service: HttpService;
  let httpSpy: Spy<HttpClient>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        HttpService,
        { provide: HttpClient, useValue: createSpyFromClass(HttpClient) }
      ]
    });

    service = TestBed.inject(HttpService);
    httpSpy = TestBed.inject<any>(HttpClient);
  });


  describe('test the getAllProducts function', () => {
    it('should return an expected list of products', () => {
      let fakeProducts: Product[] = [
        {
          id: 1,
          name: "Product one",
          items: [{ id: 1, name: "Item one" }]
        },
        {
          id: 2,
          name: "Product two",
          items: [{ id: 1, name: "Item one" }]
        }
      ];
      httpSpy.get.and.nextWith(fakeProducts);
      service.getAllProducts().subscribe({
        next:
          products => {
            expect(products).toHaveSize(fakeProducts.length);
          },
        error: err => console.log('HTTP Error', err),
      })
      expect(httpSpy.get.calls.count()).toBe(1);
    });

    it('should return a 404', () => {
      httpSpy.get.and.throwWith(new HttpErrorResponse({
        error: "404 - Not Found",
        status: 404
      }));

      service.getAllProducts().subscribe({
        next: product => { console.error("Expected a 404") },
        error:
          error => {
            expect(error.status).toEqual(404);
          }
      }
      );
      expect(httpSpy.get.calls.count()).toBe(1);
    });
  });

  describe('test the findProduct function', () => {

    let fakeProduct: Product =
    {
      id: 1,
      name: "Product one",
      items: [{ id: 1, name: "Item one" }]
    };

    it('should return the product searched', () => {
      httpSpy.get.and.nextWith(fakeProduct);
      service.findProduct(1).subscribe({
        next: product => {
          expect(product).toEqual(fakeProduct);
        },
        error: err => console.log('HTTP Error', err),
      });
      expect(httpSpy.get.calls.count()).toBe(1);
    });

    it('should return a 404', () => {

      var productId = 100;

      httpSpy.get.and.throwWith(new HttpErrorResponse({
        error: "404 - Not Found",
        status: 404
      }));

      service.findProduct(productId).subscribe({
        next: product => { console.error("Expected a 404") },
        error:
          error => {
            expect(error.status).toEqual(404);
          }
      }
      );
      expect(httpSpy.get.calls.count()).toBe(1);
    });

  });

  describe('test the findItemsProduct function', () => {

    let fakeItems: Item[] =
      [{ id: 1, name: "Item one" },
      { id: 2, name: "Item two" }
      ];

    it('should return the items of a product searched', () => {
      httpSpy.get.and.nextWith(fakeItems);
      service.findItemsProduct(1).subscribe({
        next:
          items => {
            expect(items).toEqual(fakeItems);
          },
        error: err => console.log('HTTP Error', err),
      });
      expect(httpSpy.get.calls.count()).toBe(1);
    });

    it('should return a 404', () => {

      var productId = 100;

      httpSpy.get.and.throwWith(new HttpErrorResponse({
        error: "404 - Not Found",
        status: 404
      }));

      service.findItemsProduct(productId).subscribe({
        next: product => { console.error("Expected a 404") },
        error:
          error => {
            expect(error.status).toEqual(404);
          }
      }
      );
      expect(httpSpy.get.calls.count()).toBe(1);
    });

  });

  describe('test the compareProduct function', () => {
    it('should return the comparison products result', () => {
      let fakeComparedProduct: Product =
      {
        id: 1,
        name: "Product one",
        items: [{ id: 1, name: "Item one" }]
      };
      httpSpy.get.and.nextWith(fakeComparedProduct);
      service.compareProduct(1).subscribe({
        next:
          comparedProduct => {
            expect(comparedProduct).toEqual(fakeComparedProduct);
          },
        error: err => console.log('HTTP Error', err)
      });
      expect(httpSpy.get.calls.count()).toBe(1);
    });

    it('should return a 404', () => {

      var productId = 100;

      httpSpy.get.and.throwWith(new HttpErrorResponse({
        error: "404 - Not Found",
        status: 404
      }));

      service.compareProduct(productId).subscribe({
        next: product => { console.error("Expected a 404") },
        error:
          error => {
            expect(error.status).toEqual(404);
          }
      }
      );
      expect(httpSpy.get.calls.count()).toBe(1);
    });
  });

  describe('test the searchProduct function', () => {
    it('should return the products that fits in the search', () => {
      let fakeSearchedProduct: Product =
      {
        id: 1,
        name: "Product two",
        items: [{ id: 1, name: "Item two" }]
      };
      httpSpy.get.and.nextWith(fakeSearchedProduct);
      service.productSearch("two").subscribe({
        next:
          comparedProduct => {
            expect(comparedProduct).toEqual(fakeSearchedProduct);
          },
        error: err => console.log('HTTP Error', err)
      });
      expect(httpSpy.get.calls.count()).toBe(1);
    });

    it('should return a 404', () => {

      var search = "100";

      httpSpy.get.and.throwWith(new HttpErrorResponse({
        error: "404 - Not Found",
        status: 404
      }));

      service.productSearch(search).subscribe({
        next: product => { console.error("Expected a 404") },
        error:
          error => {
            expect(error.status).toEqual(404);
          }
      }
      );
      expect(httpSpy.get.calls.count()).toBe(1);
    });
  });
});
