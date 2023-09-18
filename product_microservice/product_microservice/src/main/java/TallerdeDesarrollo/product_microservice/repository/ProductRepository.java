package TallerdeDesarrollo.product_microservice.repository;

import TallerdeDesarrollo.product_microservice.entity.ProductEntity;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface ProductRepository extends MongoRepository<ProductEntity, String> {


}
