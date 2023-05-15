import { Item } from './item.model';

export interface Product {
  id: number;
  name: string;
  items: Item[]
}

