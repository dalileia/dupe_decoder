import { ComparedProduct } from './compared.products';
import { Product } from './product.model';


export interface ComparedProductComplete {
  product: Product;
  comparedProducts: ComparedProduct[];
}
